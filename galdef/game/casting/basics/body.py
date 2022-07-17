from game.shared.point import Point
from game.casting.basics.rectangle import Rectangle

class Body:
    def __init__(self, position = Point(), size = Point(), velocity = Point()):
        self._position = position
        self._size = size
        self._velocity = velocity

    def get_position(self):
        return self._position

    def get_size(self):
        return self._size

    def get_velocity(self):
        return self._velocity

    def get_rectangle(self):
        return Rectangle(self._position, self._size)

    def set_position(self, position):
        self._position = position

    def set_size(self, size):
        self._size = size

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_center(self):
        x = self._position.get_x() + (self._size.get_x() / 2)
        y = self._position.get_y() + (self._size.get_y() / 2)
        return Point(x, y)

    def get_left(self):
        return self._position.get_x()
    
    def get_right(self):
        return self._position.get_x() + self._size.get_x()
    
    def get_top(self):
        return self._position.get_y()
    
    def get_bottom(self):
        return self._position.get_y() + self._size.get_y()

    def center_on(self, point):
        x = point.get_x() - self._size.get_x() / 2
        y = point.get_y() - self._size.get_y() / 2
        self._position = Point(x, y)