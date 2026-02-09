import wave
from array import array

class Sound:
    samples = None
    nb_samples = 0

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(self.filename, mode="rb")
        self.nb_samples = wav_file.getnframes()
        frames = wav_file.readframes(self.nb_samples)
        self.samples = array('h', frames)
        

class SoundKit:
    sounds = ()

    def get_nb_tracks(self):    
        return len(self.sounds)

class SoundKit1(SoundKit):
    sounds=(Sound("sounds/kit1/kick1.wav", "KICK1"),
            Sound("sounds/kit1/clap1.wav", "CLAP1"),
            Sound("sounds/kit1/pop1.wav", "POP1"),
            Sound("sounds/kit1/snare1.wav", "SNARE1"))

class SoundKitService:
    soundKit = SoundKit1()

    def get_nb_tracks(self):
        return self.soundKit.get_nb_tracks()

    def get_sound_at(self, index):
        if index >= len(self.soundKit.sounds):
            return None
    
        return self.soundKit.sounds[index]