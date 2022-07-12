import config
from game.casting.actor import Actor
from game.shared.point import Point

class Cycle(Actor):
    """
    A lightcycle a "A video game created motorbike".
    
    The responsibility of cycle is to move itself. And to grow a trail.

    Attributes:
        _player_num (int): The number of cycles
        _player_count (int): The number of cycles
        _segments (list): The amount of segemnts there are currently 
        _cycle_collision (boolean): Boolean to check if a collision has occurred
    """
    def __init__(self, player_num: int = 0, player_count: int = 2):
        super().__init__()
        self._player_num = player_num
        self._player_count = player_count
        self._segments = []
        self._cycle_collision = False
     
        match player_num:
            case 0:
                self._primary_color = config.GREEN
            case 1:
                self._primary_color = config.RED
            case 2:
                self._primary_color = config.BLUE
            case 3:
                self._primary_color = config.YELLOW
            
        self._prepare_body()
    
    def set_cycle_collision_bool_true(self):
        """Sets the collision boolean to true
        """
        if self._cycle_collision == False:
            self._cycle_collision = True
          
    def set_cycle_collision_bool_False(self):
        """Sets the collision boolean to true
        """

        if self._cycle_collision == True:
            self._cycle_collision = False
       
    def get_segments(self):
        """ Gets the segments list
        """
        return self._segments

    def move_next(self):
        """ Moves the cycle forward to the next space and calls the grow tail method
        """

        self._segments[0].move_next()

        self.grow_tail()

    def get_head(self):
        """ Gets the head of the cycle. (First possition in the segments list)
        """
        return self._segments[0]

    def grow_tail(self):
        """ Grows the trail of the cycles.

        Args:
            number_of_segments (int): Number of segemnts to grow each game loop
        """
        head = self._segments[0]
        segment = Actor()
        position = head.get_position().add(head.get_velocity().reverse())
        segment.set_position(position)
        segment.set_text("#")
        if self._cycle_collision:
            segment.set_color(config.WHITE)
        else:
            segment.set_color(self._primary_color)
        self._segments.append(segment)

    def turn_head(self, velocity):
        """Turnes the head of the cycle.

        Args:
            velocity (tuple): A Point tuple representing the direction the cycle is moving.
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """ Contructs the cycle: Position, velocity, text, color, etc...
        """
        head = Actor()
        x = int(config.COLUMNS * (self._player_num + 1)/(self._player_count + 1))
        y = int(config.ROWS / 2)
        position = Point(x, y).scale(config.CELL_SIZE)
        head.set_position(position)
        head.set_velocity(Point(0, -config.CELL_SIZE))
        head.set_text("@")
        head.set_color(config.WHITE)

        self._segments.append(head)

    def reset_body(self):
        """ Resets some cycle attributes
        """
        self._segments = []
        self._prepare_body()
        self._cycle_collision = False