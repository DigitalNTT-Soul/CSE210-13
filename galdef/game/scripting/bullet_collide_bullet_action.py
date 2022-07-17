from config import*
import random
from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.explosion import Explosion
from game.casting.basics.animation import Animation

from game.scripting.action import Action
from game.shared.point import Point

class BulletCollideBulletAction(Action):

    def __init__(self, physics_service, sound_service):
        self._physics_service = physics_service
        self._sound_service = sound_service
       
        
    def execute(self, cast, script):
        alien_bullets = cast.get_actors(ALIEN_PROJECTILE_GROUP)
        ship_bullets = cast.get_actors(SHIP_PROJECTILE_GROUP)
        
        for alien_bullet in alien_bullets:
            alien_bullet_body = alien_bullet.get_body()

            for ship_bullet in ship_bullets:  
                ship_bullet_body = ship_bullet.get_body()        

                if self._physics_service.has_collided(alien_bullet_body, ship_bullet_body):
                    sound_num = random.randint(0, len(EXPLOSION_SOUNDS)-1)
                    sound = EXPLOSION_SOUNDS[sound_num]
                    self._sound_service.play_sound(sound)
        
                    ship_bullet_position = ship_bullet_body.get_position() 
                    ship_bullet_x = ship_bullet_position.get_x()
                    ship_bullet_y = ship_bullet_position.get_y()
                    explosion_x = ship_bullet_x + (PROJECTILE_WIDTH - EXPLOSION_WIDTH) / 2
                    explosion_y = ship_bullet_y + (PROJECTILE_HEIGHT - EXPLOSION_HEIGHT) / 2
                    explosion_position = Point(explosion_x, explosion_y)
                    size = Point(EXPLOSION_WIDTH, EXPLOSION_HEIGHT)
                    velocity = Point(0, 0)
                    body = Body(explosion_position, size, velocity)
                    animation = Animation(EXPLOSION_IMAGES["explosions"])
                    explosion = Explosion(body, animation)  
                    cast.remove_actor(SHIP_PROJECTILE_GROUP, ship_bullet)
                    cast.remove_actor(ALIEN_PROJECTILE_GROUP, alien_bullet)
                    cast.add_actor(EXPLOSION_GROUP, explosion)
                    