from game.shared.point import Point

class Rectangle:

    def __init__(self, position = Point(), size = Point()):
        self._position = position
        self._size = size

    def get_position(self):
        return self._position
    
    def get_size(self):
        return self._size