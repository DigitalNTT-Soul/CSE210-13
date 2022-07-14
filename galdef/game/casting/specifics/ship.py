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
        velocity = self._body.get_velocity()
        position = self._body.get_position().add(velocity)
        
        x = position.get_x()
        if x < 0:
            position = Point(0, position.get_y())
        elif x > (MAX_X - SHIP_WIDTH):
            position = Point(MAX_X - SHIP_WIDTH, position.get_y())

        self._body.set_position(position)

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