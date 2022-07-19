from config import *
from game.scripting.action import Action

class IncreaseDecreaseVolumeAction(Action):
    def __init__(self, keyboard_service, sound_service):
        self._keyboard_service = keyboard_service
        self._sound_service = sound_service

    def execute(self, cast, script, flags):
        if self._keyboard_service.is_key_pressed(PLUS):
            self._sound_service.increase_volume()
        elif self._keyboard_service.is_key_pressed(MINUS):
            self._sound_service.decrease_volume()