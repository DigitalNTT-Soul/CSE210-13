import pyray
from game.services.keyboard_service import KeyboardService


class RaylibKeyboardService(KeyboardService):
    """A Raylib implementation of KeyboardService."""

    def __init__(self):
        self._keys = {}
        self._keys["a"] = pyray.KEY_A
        self._keys["b"] = pyray.KEY_B
        self._keys["c"] = pyray.KEY_C
        self._keys["d"] = pyray.KEY_D
        self._keys["e"] = pyray.KEY_E
        self._keys["f"] = pyray.KEY_F
        self._keys["g"] = pyray.KEY_G
        self._keys["h"] = pyray.KEY_H
        self._keys["i"] = pyray.KEY_I
        self._keys["j"] = pyray.KEY_J
        self._keys["k"] = pyray.KEY_K
        self._keys["l"] = pyray.KEY_L
        self._keys["m"] = pyray.KEY_M
        self._keys["n"] = pyray.KEY_N
        self._keys["o"] = pyray.KEY_O
        self._keys["p"] = pyray.KEY_P
        self._keys["q"] = pyray.KEY_Q
        self._keys["r"] = pyray.KEY_R
        self._keys["s"] = pyray.KEY_S
        self._keys["t"] = pyray.KEY_T
        self._keys["u"] = pyray.KEY_U
        self._keys["v"] = pyray.KEY_V
        self._keys["w"] = pyray.KEY_W
        self._keys["x"] = pyray.KEY_X
        self._keys["y"] = pyray.KEY_Y
        self._keys["z"] = pyray.KEY_Z
        self._keys["0"] = pyray.KEY_ZERO
        self._keys["1"] = pyray.KEY_ONE
        self._keys["2"] = pyray.KEY_TWO
        self._keys["3"] = pyray.KEY_THREE
        self._keys["4"] = pyray.KEY_FOUR
        self._keys["5"] = pyray.KEY_FIVE
        self._keys["6"] = pyray.KEY_SIX
        self._keys["7"] = pyray.KEY_SEVEN
        self._keys["8"] = pyray.KEY_EIGHT
        self._keys["9"] = pyray.KEY_NINE
        self._keys["left"] = pyray.KEY_LEFT
        self._keys["right"] = pyray.KEY_RIGHT
        self._keys["up"] = pyray.KEY_UP
        self._keys["down"] = pyray.KEY_DOWN
        self._keys["enter"] = pyray.KEY_ENTER
        self._keys["space"] = pyray.KEY_SPACE

    def is_key_down(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_pressed(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_released(raylib_key)
    
    def is_key_up(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)