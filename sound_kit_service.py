
class Sound:
    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname

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