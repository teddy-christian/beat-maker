import sys
import os
import wave
from array import array


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


class Sound:
    samples = None
    nb_samples = 0

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(resource_path(self.filename), mode="rb")
        self.nb_samples = wav_file.getnframes()
        frames = wav_file.readframes(self.nb_samples)
        self.samples = array('h', frames)


class SoundKit:
    sounds = ()

    def get_nb_tracks(self):
        return len(self.sounds)

    def get_all_samples(self):
        all_samples = []
        for i in range(0, len(self.sounds)):
            all_samples.append(self.sounds[i].samples)
        return all_samples

class SoundKit1(SoundKit):
    sounds=(Sound("sounds/kit1/kick1.wav",    "KICK 1"),
            Sound("sounds/kit1/kick2.wav",    "KICK 2"),
            Sound("sounds/kit1/kick3.wav",    "KICK 3"),
            Sound("sounds/kit1/kick4.wav",    "KICK 4"),
            Sound("sounds/kit1/kick5.wav",    "KICK 5"),
            Sound("sounds/kit1/snare1.wav",   "SNARE"),
            Sound("sounds/kit1/clap1.wav",    "CLAP"),
            Sound("sounds/kit1/crack1.wav",   "CRACK"),
            Sound("sounds/kit1/hat1.wav",     "HAT 1"),
            Sound("sounds/kit1/hat2.wav",     "HAT 2"),
            Sound("sounds/kit1/hat3.wav",     "HAT 3"),
            Sound("sounds/kit1/hat4.wav",     "HAT 4"),
            Sound("sounds/kit1/hat.wav",      "HAT"),
            Sound("sounds/kit1/chick1.wav",   "CHICK 1"),
            Sound("sounds/kit1/chick2.wav",   "CHICK 2"),
            Sound("sounds/kit1/chick3.wav",   "CHICK 3"),
            Sound("sounds/kit1/chick4.wav",   "CHICK 4"),
            Sound("sounds/kit1/boom1.wav",    "BOOM 1"),
            Sound("sounds/kit1/boom2.wav",    "BOOM 2"),
            Sound("sounds/kit1/boom3.wav",    "BOOM 3"),
            Sound("sounds/kit1/boom4.wav",    "BOOM 4"),
            Sound("sounds/kit1/boomba.wav",   "BOOMBA"),
            Sound("sounds/kit1/boomboom.wav", "BOOMBOOM"),
            Sound("sounds/kit1/boomhaa1.wav", "BOOMHAA"),
            Sound("sounds/kit1/longboom.wav", "LONGBOOM"),
            Sound("sounds/kit1/pop1.wav",     "POP 1"),
            Sound("sounds/kit1/pop2.wav",     "POP 2"),
            Sound("sounds/kit1/click1.wav",   "CLICK 1"),
            Sound("sounds/kit1/click2.wav",   "CLICK 2"),
            Sound("sounds/kit1/hiss1.wav",    "HISS 1"),
            Sound("sounds/kit1/hiss2.wav",    "HISS 2"),
            Sound("sounds/kit1/hiss3.wav",    "HISS 3"),
            Sound("sounds/kit1/breath1.wav",  "BREATH 1"),
            Sound("sounds/kit1/breath2.wav",  "BREATH 2"),
            Sound("sounds/kit1/breath.wav",   "BREATH"),
            Sound("sounds/kit1/buff1.wav",    "BUFF"),
            Sound("sounds/kit1/ahh1.wav",     "AHH 1"),
            Sound("sounds/kit1/ahh2.wav",     "AHH 2"),
            Sound("sounds/kit1/ahh3.wav",     "AHH 3"),
            Sound("sounds/kit1/ha.wav",       "HA"),
            Sound("sounds/kit1/catchit.wav",  "CATCHIT"),
            Sound("sounds/kit1/huhuhpoof.wav","HUHUHPOOF"),
            Sound("sounds/kit1/pasis.wav",    "PASIS"),
            Sound("sounds/kit1/wawa.wav",     "WAWA"))

class SoundKitService:
    soundKit = SoundKit1()

    def get_nb_tracks(self):
        return self.soundKit.get_nb_tracks()

    def get_sound_at(self, index):
        if index >= len(self.soundKit.sounds):
            return None
        return self.soundKit.sounds[index]