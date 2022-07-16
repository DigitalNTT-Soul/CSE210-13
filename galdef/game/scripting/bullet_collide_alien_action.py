from config import *
from random import randint
from game.scripting.action import Action


class BulletCollideAlienAction(Action):

    def __init__(self, physics_service, sound_service):
        self._physics_service = physics_service
        self._sound_service = sound_service
        
    def execute(self, cast, script):
        bullet = cast.get_first_actor(PROJECTILE_GROUP)
        aliens = cast.get_actors(ALIEN_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
    
        pass
        # for alien in aliens:
        #     bullet_body = bullet.get_body()
        #     alien_body = aliens.get_body()

        #     if self._physics_service.has_collided(bullet_body, alien_body):
               
        #         sound_num = randint(0, len(EXPLOSION_SOUNDS)-1)
        #         sound = EXPLOSION_SOUNDS[sound_num]
        #         self._sound_service.play_sound(sound)
        #         points = alien.get_points()
        #         stats.add_points(points)
        #         cast.remove_actor(ALIEN_GROUP, alien)
        #         cast.remove_actor(PROJECTILE_GROUP, bullet)