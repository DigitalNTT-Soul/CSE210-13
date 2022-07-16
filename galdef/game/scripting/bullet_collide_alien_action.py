from config import *
from random import randint
from game.scripting.action import Action


class BulletCollideAlienAction(Action):

    def __init__(self, physics_service, sound_service):
        self._physics_service = physics_service
        self._sound_service = sound_service
        
    def execute(self, cast, script):
        bullets = cast.get_actors(PROJECTILE_GROUP)
        if bullets == []:
            return
        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        if alien_grid == []:
            return
        stats = cast.get_first_actor(STATS_GROUP)
        
        for bullet in bullets:
            for row in alien_grid:
                for alien in row:
                    bullet_body = bullet.get_body()
                    alien_body = alien.get_body()

                    if self._physics_service.has_collided(bullet_body, alien_body):
                        sound_num = randint(0, len(EXPLOSION_SOUNDS)-1)
                        sound = EXPLOSION_SOUNDS[sound_num]
                        self._sound_service.play_sound(sound)
                        points = alien.get_points()
                        stats.add_points(points)
                        stats.add_kill()
                        cast.remove_actor(PROJECTILE_GROUP, bullet)
                        # remove alien actor from grid, but not from cast.
                        row.remove(alien)
                        if row == []:
                            alien_grid.remove(row)