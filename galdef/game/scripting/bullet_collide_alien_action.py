from config import *
from random import randint

from game.scripting.action import Action

from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.explosion import Explosion
from game.casting.basics.animation import Animation

from game.scripting.action import Action
from game.shared.point import Point

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
                         # RYAN' playing with adding explosions...
                    # comment out group below so stop the mess!!!
                        alien_position = alien.get_body().get_position()
                        alien_x = alien_position.get_x()
                        alien_y = alien_position.get_y()
                        explosion_x = alien_x + (ALIEN_WIDTH - EXPLOSION_WIDTH) / 2
                        explosion_y = alien_y + (ALIEN_HEIGHT - EXPLOSION_HEIGHT) / 2
                        explosion_position = Point(explosion_x, explosion_y)
                        size = Point(EXPLOSION_WIDTH, EXPLOSION_HEIGHT)
                        velocity = Point(0, EXPLOSION_VELOCITY)
                        body = Body(explosion_position, size, velocity)
                        animation = Animation(EXPLOSION_IMAGES["explosions"])
                        explosion = Explosion(body, animation, alien)  
                        cast.add_actor(EXPLOSION_GROUP, explosion)
                        # cast.remove_actor(EXPLOSION_GROUP, explosion)


                        

                        

                        