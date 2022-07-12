from config import Config
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.debris import Debris

from game.shared.color import Color
from game.shared.point import Point 

from random import randint


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        
        self._config = Config()

        self._keyboard_service = KeyboardService(self._config.get_cell_size())
        self._video_service = VideoService(
            self._config.get_window_title(),
            self._config.get_max_width(),
            self._config.get_max_height(),
            self._config.get_cell_size(),
            self._config.get_target_framerate()
        )
        
        self._gravity_vector = Point(0,self._config.get_cell_size())
        self._gravity_frame = 0

        self._score = 0

    def start_game(self):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        cast = Cast()
        cast.add_actor("player",Actor("#", self._config.get_cell_size(),Color(255,255,255),Point(int(self._config.get_max_width() / 2), int(self._config.get_max_height() - self._config.get_cell_size()))))
        cast.add_actor("banner",Actor("",self._config.get_cell_size(), Color(255,255,255),Point(self._config.get_cell_size(),0)))

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banner")
        player = cast.get_first_actor("player")

        #jump 
        if (player.get_velocity().get_y() == -self._config.get_cell_size() * self._config.get_jump_height() and
            player.get_position().get_y() != self._config.get_max_height() - self._config.get_cell_size()):

            player.set_velocity(Point(player.get_velocity().get_x(),0))
        
        banner.set_text("")
        player.move_next(self._config.get_max_width(), self._config.get_max_height())
        
        # implementing gravity here
        self._gravity_frame = (self._gravity_frame + 1) % self._config.get_gravity_frames_per_tick()

        for actor in cast.get_all_actors():
            if isinstance(actor, Debris) and player.get_position().equals(actor.get_position()):
                self._score += actor.get_value()
                cast.remove_actor("debris", actor)

            elif not self._gravity_frame:
                # delete/garbage-collect actors that go under the floor
                actor_on_floor = (actor.get_position().get_y() == self._config.get_max_height() - self._config.get_cell_size())
                if isinstance(actor, Debris) and actor_on_floor:
                    cast.remove_actor("debris", actor)
                elif actor is not banner and not actor_on_floor:
                    actor.set_velocity(Point(0, self._config.get_cell_size()))
                    actor.move_next(self._config.get_max_width(), self._config.get_max_height())

        if not self._gravity_frame:
            for i in range(randint(1,3)):
                if randint(0,1):
                    cast.add_actor("debris", Debris(1,"*", Point(randint(0,self._config.get_column_count() - 1),1).scale(self._config.get_cell_size())))
                else:
                    cast.add_actor("debris", Debris(-1,"o", Point(randint(0,self._config.get_column_count() - 1),1).scale(self._config.get_cell_size())))

        banner.set_text(f"S C O R E : {self._score}")        
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()