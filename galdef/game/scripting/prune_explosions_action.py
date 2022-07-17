
from config import *

from game.scripting.action import Action
from game.scripting.action import Action

class PruneExposionsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script):
        # alien_position = alien.get_body().get_position()
        # alien_x = alien_position.get_x()
        # alien_y = alien_position.get_y()
        # explosion_x = alien_x + (ALIEN_WIDTH - EXPLOSION_WIDTH) / 2
        # explosion_y = alien_y + (ALIEN_HEIGHT - EXPLOSION_HEIGHT) / 2
        # explosion_position = Point(explosion_x, explosion_y)
        # size = Point(EXPLOSION_WIDTH, EXPLOSION_HEIGHT)
        # velocity = Point(0, EXPLOSION_VELOCITY)
        # body = Body(explosion_position, size, velocity)
        # animation = Animation(EXPLOSION_IMAGES["explosions"])
        
        explosions = cast.get_actors(EXPLOSION_GROUP)
        for explosion in explosions:
            cast.remove_actor(EXPLOSION_GROUP, explosion)