
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

TRACK_NB_STEPS = 16

class TrackStepButton(ToggleButton):
    pass

class TrackSoundButton(Button):
    pass

class TrackWidget(BoxLayout):
    sound_kit_service = ObjectProperty()
    
    def __init__(self, sound, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        self.add_widget(sound_button)
        for i in range(0, TRACK_NB_STEPS):
            self.add_widget(TrackStepButton())