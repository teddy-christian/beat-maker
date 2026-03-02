import sys
import os

def resource_path(relative_path):
    """Return the absolute path to a bundled resource.
    Works both in development (normal Python) and when frozen by PyInstaller.
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

from kivy.config import Config
Config.set('graphics', 'width',  '600')
Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, Clock
from track import TrackWidget
from sound_kit_service import SoundKitService
from audio_engine import AudioEngine

Builder.load_file(resource_path("track.kv"))
Builder.load_file(resource_path("play_indicator.kv"))

TRACK_NB_STEPS = 16
MIN_BPM = 80
MAX_BPM = 160

class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    play_indicator_widget = ObjectProperty()
    TRACK_STEPS_LEFT_ALIGN = NumericProperty(dp(100))
    step_index = 0
    bpm = NumericProperty(120)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()
        self.audio_engine = AudioEngine()
        self.mixer = self.audio_engine.create_mixer(self.sound_kit_service.soundKit.get_all_samples(), 120, TRACK_NB_STEPS, self.on_mixer_current_step_changed, MIN_BPM)

    def on_parent(self, widget, parent):
        self.play_indicator_widget.set_nb_steps(TRACK_NB_STEPS)
        for i in range(self.sound_kit_service.get_nb_tracks()):
            sound = self.sound_kit_service.get_sound_at(i)
            self.tracks_layout.add_widget(TrackWidget(sound, self.audio_engine, TRACK_NB_STEPS, self.mixer.tracks[i], self.TRACK_STEPS_LEFT_ALIGN))

    def on_mixer_current_step_changed(self, step_index):
        self.step_index = step_index
        Clock.schedule_once(self.update_play_indicator_cbk, 0)

    def update_play_indicator_cbk(self, dt):
        if self.play_indicator_widget is not None:
            self.play_indicator_widget.set_current_step_index(self.step_index)

    def on_play_button_pressed(self):
        self.mixer.audio_play()

    def on_stop_button_pressed(self):
        self.mixer.audio_stop()

    def on_bpm(self, widget, value):
        if value < MIN_BPM:
            self.bpm = MIN_BPM
            return
        if value > MAX_BPM:
            self.bpm = MAX_BPM
            return
        self.mixer.set_bpm(self.bpm)

class MrBeatApp(App):
    kv_file = resource_path("mrbeat.kv")

MrBeatApp().run()