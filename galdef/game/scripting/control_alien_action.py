from config import *
from game.scripting.action import Action


class ControlAlienAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script):
        aliens = cast.get_actors(ALIEN_GROUP)            
        for alien in aliens:
            pass
    #         # alien.march_right()
    #         alien.move_next()

