from config import *
from game.scripting.action import Action

class PruneMissedShotsAction(Action):
    def __init__(self):
        pass

    def execute(self, cast, script):
        self._prune(cast, ALIEN_PROJECTILE_GROUP)
        self._prune(cast, SHIP_PROJECTILE_GROUP)

    def _prune(self, cast, group):
        bullets = cast.get_actors(group)

        for bullet in bullets:
            bullet_position = bullet.get_body().get_position()
            bullet_x = bullet_position.get_x()
            bullet_y = bullet_position.get_y()

            if bullet_x < 0 or MAX_X < bullet_x or bullet_y < 0 or MAX_Y < bullet_y:
                cast.remove_actor(group, bullet)