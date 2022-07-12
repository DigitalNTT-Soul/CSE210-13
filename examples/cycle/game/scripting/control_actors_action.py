import config
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle import Cycle

class ControlActorsAction(Action):
    """-
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
        self._left = Point(-config.CELL_SIZE, 0)
        self._right = Point(config.CELL_SIZE, 0)
        self._up = Point(0, -config.CELL_SIZE)
        self._down = Point(0, config.CELL_SIZE)
        self._key_chart = [
            ['w','a','s','d'],
            ['i','j','k','l'],
            ['t','f','g','h'],
            ['up_arrow','left_arrow','down_arrow','right_arrow']
        ]

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """ 
        
        cycles = cast.get_actors("cycles")

        for i in range(len(cycles)):
            head_velocity = cycles[i].get_head().get_velocity()
            direction = Point(0,0)
            if head_velocity == self._left or head_velocity == self._right:
                if self._keyboard_service.is_key_down(self._key_chart[i][0]):
                    direction = direction.add(self._up)
                if self._keyboard_service.is_key_down(self._key_chart[i][2]):
                    direction = direction.add(self._down)
            if head_velocity == self._up or head_velocity == self._down:
                if self._keyboard_service.is_key_down(self._key_chart[i][1]):
                    direction = direction.add(self._left)
                if self._keyboard_service.is_key_down(self._key_chart[i][3]):
                    direction = direction.add(self._right)
            if direction != Point(0,0):
                cycles[i].turn_head(direction)