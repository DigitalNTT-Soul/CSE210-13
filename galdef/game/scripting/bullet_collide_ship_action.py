from config import*
import random
from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.explosion import Explosion
from game.casting.basics.animation import Animation

from game.scripting.action import Action
from game.shared.point import Point

class BulletCollideShipAction(Action):

    def __init__(self, physics_service, sound_service):
        self._physics_service = physics_service
        self._sound_service = sound_service
       
        
    def execute(self, cast, script):
        bullets = cast.get_actors(ALIEN_PROJECTILE_GROUP)
        if bullets == []:
            return
        ship = cast.get_first_actor(SHIP_GROUP)
        if not ship:
            return
        stats = cast.get_first_actor(STATS_GROUP)
        
        for bullet in bullets:
            bullet_body = bullet.get_body()
            ship_body = ship.get_body()        

            if self._physics_service.has_collided(bullet_body, ship_body):
                sound_num = random.randint(0, len(EXPLOSION_SOUNDS)-1)
                sound = EXPLOSION_SOUNDS[sound_num]
                self._sound_service.play_sound(sound)

                # remove ship actor from grid, but not from cast.
        
                ship_position = ship_body.get_position() 
                ship_x = ship_position.get_x()
                ship_y = ship_position.get_y()
                explosion_x = ship_x + (SHIP_WIDTH - EXPLOSION_WIDTH) / 2
                explosion_y = ship_y + (SHIP_HEIGHT - EXPLOSION_HEIGHT) / 2
                explosion_position = Point(explosion_x, explosion_y)
                size = Point(EXPLOSION_WIDTH, EXPLOSION_HEIGHT)
                velocity = Point(0, 0)
                body = Body(explosion_position, size, velocity)
                animation = Animation(EXPLOSION_IMAGES["explosions"])
                explosion = Explosion(body, animation, ship)  
                cast.remove_actor(SHIP_GROUP, ship)
                cast.remove_actor(ALIEN_PROJECTILE_GROUP, bullet)
                cast.add_actor(EXPLOSION_GROUP, explosion)
                