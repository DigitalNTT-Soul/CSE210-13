from config import *
from game.scripting.action import Action

class ToggleHardcoreModeAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script):
        if self._keyboard_service.is_key_pressed(HARDCORE):
            hardcore_status = cast.get_first_actor(HARDCORE)
            hardcore_status[0] = not (hardcore_status[0])