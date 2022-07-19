from config import *

class Flags:
    def __init__(self):
        self._flags = {}

    def get_flag(self, key):
        result = None
        if key in self._flags.keys():
            result = self._flags[key]
        return result

    def set_flag(self, key, value):
        self._flags[key] = value

    def toggle_flag(self, key):
        if key in self._flags.keys():
            self._flags[key] = not self._flags[key]