from game.casting.point import Point


class Rectangle:
    """A 4-sided flat shape with straight sides."""

    def __init__(self, position, size):
        """Constructs a new Rectangle."""
        self._position = Point()
        self._size = Point() 

    def get_position(self):
        """Gets the top left point of the rectangle.
        
        Returns:
            An instance of Point containing the top left coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the size of the rectangle.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._size