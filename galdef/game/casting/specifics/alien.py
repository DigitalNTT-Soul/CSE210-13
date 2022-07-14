from config import *
from game.casting.basics.actor import Actor
from game.shared.point import Point

class Alien(Actor):
    def __init__(self, body, animation, level_speed, debug = False):
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._level_speed = level_speed

    #########################
    # Body Handling Section #
    #########################
    def get_body(self):
        return self._body

    def move_next(self):
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def march_left(self):
        velocity = Point(-self._level_speed, 0)
        self._body.set_velocity(velocity)

    def march_right(self):
        velocity = Point(self._level_speed, 0)
        self._body.set_velocity(velocity)

    def march_forward(self):
        velocity = Point(0, self._level_speed)
        self._body.set_velocity(velocity)

    ##############################
    # Animation Handling Section #
    ##############################
    def get_animation(self):
        return self._animation