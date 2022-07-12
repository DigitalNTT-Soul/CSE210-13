import os
import pathlib
import pyray
from game.services.audio_service import AudioService 


class RaylibAudioService(AudioService):
    """A Raylib implementation of AudioService."""

    def __init__(self):
        self._sounds = {}
        
    def initialize(self):
        pyray.init_audio_device()
        
    def load_sounds(self, directory):
        filepaths = self._get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            sound = pyray.load_sound(filepath)
            self._sounds[filepath] = sound

    def play_sound(self, sound):
        filepath = sound.get_filename()
        # fixed os dependent filepath
        filepath = str(pathlib.Path(filepath))
        volume = sound.get_volume()
        sound = self._sounds[filepath]
        # pyray.set_sound_volume(volume)
        pyray.play_sound(sound)
    
    def release(self):
        pyray.close_audio_device()
        
    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
        
    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths