import pygame
import os


class SoundService:
    """ Loads Music and sounds to be used in game.
    """

    def __init__(self):
        self._freq = 44100
        self._bitsize = -16
        self._channels = 2
        self._buffer = 1024
        pygame.mixer.init(self._freq, self._bitsize, self._channels, self._buffer)
        pygame.mixer.music.set_volume(0.4)

        # Load music
        self._path_for_tron = os.path.abspath(__file__)
        self._tron_file_path = os.path.join(os.path.dirname(self._path_for_tron), 'music/Tron.mp3')
        pygame.mixer.music.load(self._tron_file_path)

    def play_music(self):
        """ Plays the music
        """
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

    def play_wilhelm(self):
        """ Plays the collision sound
        """
        self._path_for_wil = os.path.abspath(__file__)
        self._wil_file_path = os.path.join(os.path.dirname(self._path_for_wil), 'music/wilhelmscream.mp3')
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self._wil_file_path))

    def stop_music(self):
        """ Stops the music playing
        """
        pygame.mixer.music.stop()
      



