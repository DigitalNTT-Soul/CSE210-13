import config
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.sound_service import SoundService

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction.
        """
        self._first_collision = False
        self._tie = False
        self._give_point_collision = False
        self._is_game_over = False
        self._new_round_message = False
        self._sound_service = SoundService()
        self._message = Actor()

    def get_game_over_bool(self):
        """ Gets the game over boolean
        """
        return self._is_game_over

    def get_first_collision_bool(self):
        """ Gets the first collision boolean
        """
        return self._first_collision

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_actors("cycles")
        cycle0 = cycles[0]
        cycle1 = cycles[1]

        head0 = cycle0.get_segments()[0]
        segments0 = cycle0.get_segments()[1:]

        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]

        if self._tie == False:
            if self._new_round_message == False:
                self._message.set_text(" ") 

        for segment in segments0:
            if head0.get_position().equals(head1.get_position()):
                self._tie = True
                self._handle_tie_condition(cast)

        for segment in segments1:
            if head1.get_position().equals(head0.get_position()):
                self._tie = True
                self._handle_tie_condition(cast)

        for segment in segments0:
            if head0.get_position().equals(segment.get_position()):
                self._handle_game_over(cast, cycles)
                self._handle_points(cast, 1)

        for segment in segments0:
            if head1.get_position().equals(segment.get_position()):
                self._handle_game_over(cast, cycles)
                self._handle_points(cast, 0)

        for segment in segments1:
            if head0.get_position().equals(segment.get_position()):
                self._handle_game_over(cast, cycles)
                self._handle_points(cast, 1)

        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._handle_game_over(cast, cycles)
                self._handle_points(cast, 0)
         
    def _handle_game_over(self, cast, cycles):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
            cycles (Actors): The cycles
        """

        self._new_round_message = True

        cycles = cast.get_actors("cycles")
        for cycle in cycles:
            cycle.set_cycle_collision_bool_true()

        if self._first_collision == False:
            self._sound_service.play_wilhelm()
            self._first_collision = True

        segment_sets = []
        for cycle in cycles:
            segment_sets.append(cycle.get_segments())
  
        for segment_set in segment_sets:
            for segment in segment_set:
                segment.set_color(config.WHITE)

        x = int(config.MAX_X / 2)
        y = int(config.MAX_Y / 2)
        position = Point(x, y)

        if self._tie == False:
            if self._new_round_message == True:
                
                self._message.set_text("                ROUND OVER!\n TO PLAY ANOTHER ROUND PRESS R\n  OR PRESS ESC TO EXIT THE GRID")
                self._message.set_font_size(30)
                self._message.set_color(config.YELLOW)
                self._message.set_position(position)
                cast.add_actor("messages", self._message)

    def _handle_points(self, cast, cycle_num):
        """ Handles giving points to the cycles

        Args:
            cast (Actors): All actors objects in the game
            cycle_num (int): Number of cycles
        """
        
        if self._tie == False:
            scores = cast.get_actors("scores")
            score0 = scores[0]
            score1 = scores[1]

            if cycle_num == 0:
                if self._give_point_collision == False:
                    score0.add_points(1)
                    self._give_point_collision = True

            if cycle_num == 1:
                if self._give_point_collision == False:
                    score1.add_points(1)
                    self._give_point_collision = True

    def reset_collisions(self):
        """ Resets boolean values to False. Clears messages from the screen. Resets collisions
        """
        self._first_collision = False
        self._give_point_collision = False
        self._is_game_over = False
        self._new_round_message = False
        self._tie = False

    def _handle_tie_condition(self, cast):
        """ Handles tie conditions. Displayes tie message.

        Args:
            cast (Actors): All Actor objects in the game. 
        """

        x = int(config.MAX_X / 2)
        y = int(config.MAX_Y / 2)
        position = Point(x, y)

        if self._tie == True:
            
            self._message.set_text("    YOU KNOCKED HEADS!\n      NO POINTS GIVEN\n PRESS R FOR A NEW ROUND")
            self._message.set_font_size(30)
            self._message.set_color(config.YELLOW)
            self._message.set_position(position)
            cast.add_actor("messages", self._message)