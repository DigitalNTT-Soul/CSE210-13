from game.casting.basics.actor import Actor
from game.shared.point import Point
import config


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self): #(self, player_num: int = 0, player_count: int = 2):
        super().__init__()
        # self._player_num = player_num
        # self._player_count = player_count
        self._points = 0
        self.add_points(0)
        self.set_font_size(25)
        self.set_color(config.BLUE)
        # x = player_num * int(config.MAX_X / player_count)
        # self._text = text
        # self._position = position
        # self.set_position(Point(300, 300))

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def reset_points(self):
        """ Resets the number of points earned to 0
        """
        self._points = 0

  