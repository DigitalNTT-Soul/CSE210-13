from distutils.command.install_headers import install_headers
from config import *

import random
from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.projectile import Projectile

from game.scripting.action import Action
from game.shared.point import Point

class AlienFireProjectileAction(Action):

    def __init__(self, sound_service):
        self._sound_service = sound_service
        # self._already_shot = False
        

    def execute(self, cast, script):
        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        level = cast.get_first_actor(STATS_GROUP).get_level()
        is_hardcore = cast.get_first_actor(HARDCORE)[0]
        for row in alien_grid:
            for alien in row:
                num = random.randint(1,1000)
                if (is_hardcore and num <= level) or num == 1:
                    self._sound_service.play_sound(ALIEN_BULLET_SOUND)

                    alien_position = alien.get_body().get_position()
                    alien_x = alien_position.get_x()
                    alien_y = alien_position.get_y()
                    projectile_x = alien_x + (ALIEN_WIDTH - PROJECTILE_WIDTH) / 2
                    projectile_y = alien_y + ALIEN_HEIGHT
                        
                    projectile_position = Point(projectile_x, projectile_y)
                    size = Point(PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                    velocity = Point(0, PROJECTILE_VELOCITY)

                    body = Body(projectile_position, size, velocity)
                    animation = Image(ALIEN_PROJECTILE_BULLET_IMAGE)

                    projectile = Projectile(body, animation)
                        
                    cast.add_actor(ALIEN_PROJECTILE_GROUP, projectile)