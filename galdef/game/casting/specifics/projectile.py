from config import *
from game.casting.basics.actor import Actor
from game.shared.point import Point

class Projectile(Actor):
    def __init__(self, body, animation, parent, debug = False):
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._parent = parent

    def get_body(self):
        return self._body
    
    def get_animation(self):
        return self._animation
    
    def get_parent(self):
        return self._parent

    def move_next(self):
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)