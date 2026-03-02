import time
import threading
from array import array

import sounddevice as sd

from audio_source_mixer import AudioSourceMixer
from audio_source_one_shot import AudioSourceOneShot
from audio_source_track import AudioSourceTrack

MAX_16BITS = 32767
MIN_16BITS = -32768


class _OutputStream:
    def __init__(self, buffersize):
        self.buffersize = buffersize


class AudioEngine:
    NB_CHANNELS = 1
    SAMPLE_RATE = 44100
    BUFFER_SIZE = 4096

    def __init__(self):
        self._mixer = None
        self._running = True

        fake_stream = _OutputStream(self.BUFFER_SIZE)
        self.audio_source_one_shot = AudioSourceOneShot(fake_stream)

        self._ring = bytearray()
        self._ring_lock = threading.Lock()

        self._filler_thread = threading.Thread(target=self._filler_loop, daemon=True)
        self._filler_thread.start()

        self._sd_stream = sd.RawOutputStream(
            samplerate=self.SAMPLE_RATE,
            blocksize=self.BUFFER_SIZE,
            channels=self.NB_CHANNELS,
            dtype='int16',
            callback=self._audio_callback,
        )
        self._sd_stream.start()

    def _filler_loop(self):
        silence = bytes(self.BUFFER_SIZE * 2)
        max_ahead = self.BUFFER_SIZE * 2 * 8

        while self._running:
            with self._ring_lock:
                buf_len = len(self._ring)
            if buf_len >= max_ahead:
                time.sleep(0.001)
                continue

            chunk = self._mixer.get_bytes() if self._mixer is not None else silence
            with self._ring_lock:
                self._ring.extend(chunk)

    def _audio_callback(self, outdata, frames, time_info, status):
        needed = frames * 2

        with self._ring_lock:
            available = len(self._ring)
            if available >= needed:
                mixer_bytes = bytes(self._ring[:needed])
                del self._ring[:needed]
            else:
                mixer_bytes = bytes(self._ring) + bytes(needed - available)
                self._ring.clear()

        one_shot_bytes = self.audio_source_one_shot.get_bytes()

        mixer_arr = array('h', mixer_bytes)
        one_shot_arr = array('h', one_shot_bytes)
        mixed = array('h', [
            max(MIN_16BITS, min(MAX_16BITS, a + b))
            for a, b in zip(mixer_arr, one_shot_arr)
        ])
        outdata[:] = bytes(mixed)

    def play_sound(self, wav_samples):
        self.audio_source_one_shot.set_wav_samples(wav_samples)

    def create_track(self, wav_samples, bpm):
        source_track = AudioSourceTrack(None, wav_samples, bpm, self.SAMPLE_RATE, bpm)
        source_track.start()
        return source_track

    def create_mixer(self, all_wav_samples, bpm, nb_steps, on_current_step_changed, min_bpm):
        self._mixer = AudioSourceMixer(
            None, all_wav_samples, bpm, self.SAMPLE_RATE,
            nb_steps, on_current_step_changed, min_bpm
        )
        self._mixer.start()
        return self._mixer

    def stop(self):
        self._running = False
        self._sd_stream.stop()
        self._sd_stream.close()
