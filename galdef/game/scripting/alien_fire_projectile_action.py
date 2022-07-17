from config import *

import random
from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.projectile import Projectile

from game.scripting.action import Action
from game.shared.point import Point

class AlienFireProjectileAction(Action):

    def __init__(self, keyboard_service, sound_service):
        self._keyboard_service = keyboard_service
        self._sound_service = sound_service
        # self._already_shot = False
        

    def execute(self, cast, script):
        
        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        
        
      
        for row in alien_grid:
            for alien in row:
                
                
                num = random.randint(1,100)
                
                if num == 1:
                    self._sound_service.play_sound(BULLET_SOUND)

                    alien = cast.get_first_actor(ALIEN_PROJECTILE_GROUP)
                    alien_position = alien.get_body().get_position()
                    alien_x = alien_position.get_x()
                    alien_y = alien_position.get_y()
                    projectile_x = alien_x + (ALIEN_WIDTH - PROJECTILE_WIDTH) / 2
                    projectile_y = alien_y - PROJECTILE_HEIGHT
                        
                        
                    projectile_position = Point(projectile_x, projectile_y)
                    size = Point(PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                    velocity = Point(0, PROJECTILE_VELOCITY)

                    body = Body(projectile_position, size, velocity)
                    animation = Image(ALIEN_PROJECTILE_BULLET_IMAGE)

                    projectile = Projectile(body, animation, alien)
                        
                    cast.add_actor(ALIEN_PROJECTILE_GROUP, projectile)    