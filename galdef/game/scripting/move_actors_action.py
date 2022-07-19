from config import *
from game.scripting.action import Action

class MoveActorsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, flags):
        ship = cast.get_first_actor(SHIP_GROUP)
        if not ship:
            return
        ship.move_next()

        ship_projectiles = cast.get_actors(SHIP_PROJECTILE_GROUP)
        for projectile in ship_projectiles:
            projectile.move_next()

        alien_projectiles = cast.get_actors(ALIEN_PROJECTILE_GROUP)
        for projectile in alien_projectiles:
            projectile.move_next()

        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        for row in alien_grid:
            for alien in row:
                alien.move_next()