from config import *
from game.scripting.action import Action

class MuteUnmuteAction(Action):
    def __init__(self, keyboard_service, sound_service):
        self._muted = False
        self._keyboard_service = keyboard_service
        self._sound_service = sound_service

    def execute(self, cast, script, flags):
        if self._keyboard_service.is_key_pressed(MUTE):
            self._sound_service.toggle_mute()