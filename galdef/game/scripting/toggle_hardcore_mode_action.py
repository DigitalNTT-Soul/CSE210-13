from config import *
from game.scripting.action import Action

class ToggleHardcoreModeAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script, flags):
        if self._keyboard_service.is_key_pressed(HARDCORE):
            flags.toggle_flag(HARDCORE)