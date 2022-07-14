from config import *
from game.scripting.action import Action


class ControlAlienAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script):
        aliens = cast.get_actors(ALIEN_GROUP)
        for alien in aliens:
            alien.march_forward()
            alien.move_next()