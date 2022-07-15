from config import *

from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.specifics.projectile import Projectile

from game.scripting.action import Action
from game.shared.point import Point

class PlayerFireProjectileAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        if self._keyboard_service.is_key_down(SPACE):
            ship = cast.get_first_actor(SHIP_GROUP)
            ship_position = ship.get_body().get_position()
            ship_x = ship_position.get_x()
            ship_y = ship_position.get_y()
            projectile_x = ship_x + (SHIP_WIDTH - PROJECTILE_WIDTH) / 2
            projectile_y = ship_y - PROJECTILE_HEIGHT

            projectile_position = Point(projectile_x, projectile_y)
            size = Point(PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
            velocity = Point(0, -PROJECTILE_VELOCITY)

            body = Body(projectile_position, size, velocity)
            animation = Image(PROJECTILE_BULLET_IMAGE)

            projectile = Projectile(body, animation, ship)

            cast.add_actor(PROJECTILE_GROUP, projectile)