from config import *
from game.casting.basics.actor import Actor
from game.shared.point import Point

class Ship(Actor):
    def __init__(self, body, animation, debug = False):
        super().__init__(debug)
        self._body = body
        self._animation = animation

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

    def swing_left(self):
        velocity = Point(-SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_right(self):
        velocity = Point(SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        velocity = Point(0,0)
        self._body.set_velocity(velocity)

    ##############################
    # Animation Handling Section #
    ##############################
    def get_animation(self):
        return self._animation