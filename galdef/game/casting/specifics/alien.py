from config import *
from game.casting.basics.actor import Actor
from game.shared.point import Point

class Alien(Actor):
    def __init__(self, body, animation, level, is_hardcore):
        super().__init__()
        self._body = body
        self._animation = animation
        speed_cap = 10
        if is_hardcore:
            speed_cap = 100
        self._level_speed = min(level, speed_cap)
        self._points = 50 * (level ** 2)

    def __str__(self):
        return "X"

    #########################
    # Body Handling Section #
    #########################
    def get_body(self):
        return self._body

    def move_next(self):
        velocity = self._body.get_velocity()
        position = self._body.get_position().add(velocity)
        technical_right_wall = MAX_X - self._body.get_size().get_x()

        x = position.get_x()
        if x < 0:
            position = Point(0, position.get_y())
        elif x > technical_right_wall:
            position = Point(technical_right_wall, position.get_y())

        self._body.set_position(position)

    def march_left(self):
        velocity = Point(-self._level_speed, 0)
        self._body.set_velocity(velocity)

    def march_right(self):
        velocity = Point(self._level_speed, 0)
        self._body.set_velocity(velocity)

    def march_forward(self):
        velocity = Point(0, ALIEN_HEIGHT)
        self._body.set_velocity(velocity)

    def set_specific_velocity(self, velocity):
        self._body.set_velocity(velocity)

    def get_points(self):
        return self._points
    
    def get_level_speed(self):
        return self._level_speed

    def get_height(self):
        return self._body.get_size().get_y()

    ##############################
    # Animation Handling Section #
    ##############################
    def get_animation(self):
        return self._animation