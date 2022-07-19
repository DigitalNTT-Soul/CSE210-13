from config import *
from game.scripting.action import Action

class PauseAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        if self._keyboard_service.is_key_pressed(PAUSE):
            while not self._keyboard_service.is_key_pressed(PAUSE):
                pass