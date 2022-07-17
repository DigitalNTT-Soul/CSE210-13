from config import *

from game.scripting.action import Action
from game.scripting.action import Action

class PruneExplosionsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script):        
        explosions = cast.get_actors(EXPLOSION_GROUP)
        for explosion in explosions:
            animation_frame = explosion.get_animation().get_index()
            if animation_frame == 5:
                cast.remove_actor(EXPLOSION_GROUP, explosion)