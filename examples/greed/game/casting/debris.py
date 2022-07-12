from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import randint

class Debris(Actor):
    def __init__(self, value: int, text: str, position: Point, font_size: int = 15, velocity: Point = Point(0, 0)):

        super().__init__()
        self._value = value
        self._text = text
        self._position = position
        self._velocity = velocity
        self._font_size = font_size
        self._color = Color(randint(0,255),randint(0,255),randint(0,255))
    
    def get_value(self):
        return self._value