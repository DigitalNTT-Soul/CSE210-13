import pyray
from config import *

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        # movement
        self._keys['a'] = pyray.KEY_A
        self._keys['d'] = pyray.KEY_D

        self._keys[LEFT] = pyray.KEY_LEFT
        self._keys[RIGHT] = pyray.KEY_RIGHT

        # attack
        self._keys[SPACE] = pyray.KEY_SPACE

        # restart game
        self._keys['r'] = pyray.KEY_R

        # audio
        self._keys[MUTE] = pyray.KEY_M
        self._keys[PLUS] = pyray.KEY_EQUAL # This is the actual button where the Plus Sign is on the keyboard
        self._keys[MINUS] = pyray.KEY_MINUS

        # hardcore mode
        self._keys[HARDCORE] = pyray.KEY_H

        #Pause game
        self._keys[PAUSE] = pyray.KEY_P
        

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key 
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key 
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)

    def is_key_pressed(self, key):
        """Checks if the given key has been pressed once.
        
        Args:
            key (string): The given key 
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_pressed(pyray_key)