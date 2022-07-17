import pyray
from game.shared.os_tool import OSTool
from config import *
import pathlib
from game.casting.basics.sound import Sound

class SoundService:

    def __init__(self):
        self._sounds = {}
        self._muted = False

    def initialize(self):
        pyray.init_audio_device()

    def release(self):
        pyray.close_audio_device()

    def load_sounds(self, directory):
        filepaths = OSTool.get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            self._sounds[filepath] = pyray.load_sound(filepath)
    
    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
    
    def play_sound(self, sound):
        if not isinstance(sound, Sound):
            sound = Sound(sound)
        filepath = str(pathlib.Path(sound.get_filename()))
        volume = sound.get_volume()
        sound = self._sounds[filepath]
        pyray.play_sound(sound)

    def is_sound_playing(self, sound):
        """Check if a sound is currently playing
        """
        if not isinstance(sound, Sound):
            sound = Sound(sound)
        filepath = str(pathlib.Path(sound.get_filename()))
        sound = self._sounds[filepath]
        pyray.is_sound_playing(sound)

    def toggle_mute(self):
        self._muted = not self._muted

        # CHANGE MASTER VOLUME INSTEAD OF THE BELOW

        # if self._muted:
        #     for sound in self._sounds:
        #         if self.is_sound_playing(sound):
        #             pyray.pause_sound(sound)
        # else:
        #     for sound in self._sounds:
        #         pyray.resume_sound(sound)

    # def play_sound_looped(self, sound):
    #     if not isinstance(sound, Sound):
    #         sound = Sound(sound, .5, True)
    #     filepath = str(pathlib.Path(sound.get_filename()))
    #     sound = self._sounds[filepath]
    #     pyray.play_sound(sound)