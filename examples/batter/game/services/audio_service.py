class AudioService:
    """An audio service inteface.

    The responsibility of AudioService is to handle the audio assets for a game.
    """

    def initialize(self):
        """Initializes underlying audio device."""
        raise NotImplementedError("not implemented in base class")

    def load_sounds(self, directory):
        """Loads all the sounds in the given directory and sub-directories.
        
        Args:
            directory: A string containing the absolute folder path where sound files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def play_sound(self, sound):
        """Plays the given sound.
        
        Args:
            sound: An instance of the batter.casting.Sound class.
        """
        raise NotImplementedError("not implemented in base class")

    def release(self):
        """Releases the underlying audio device."""
        raise NotImplementedError("not implemented in base class")

    def unload_sounds(self):
        """Unloads all the sounds that were previously loaded."""
        raise NotImplementedError("not implemented in base class")