from config import *
from game.casting.basics.cast import Cast
from game.casting.basics.body import Body
from game.casting.basics.animation import Animation
from game.casting.specifics.score import Score
from game.casting.specifics.ship import Ship
from game.casting.specifics.background import Background
from game.casting.basics.image import Image

from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.control_ship_action import ControlShipAction

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.sound_service import SoundService
from game.shared.point import Point




class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = KeyboardService()
        self._video_service = VideoService()
        self._sound_service = SoundService()
        self._cast = Cast() 
        self._script = Script()
        self._play_new_round = True
               

    def start_game(self):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        # while self._play_new_round:
        self._video_service.open_window()
        self._build_game()
        self._sound_service.play_music()

        while self._video_service.is_window_open():
            self._execute_actions("input")
            self._execute_actions("update")
            self._execute_actions("output")
        
        self._dismantle_game()

        self._video_service.close_window()

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script)

    def _build_game(self):
        """ Builds the game
        """
        self._video_service.load_images("galdef/assets/images")
        # self._video_service.load_fonts("galdef/assets/fonts")
        # self._sound_service.load_sounds("galdef/assets/sounds")
        self._add_background()
        self._add_ship()
        # add aliens
        # add level, score, and lives counters

        # Come up with input, update, and output actions to script
        self._script.add_action("update", ControlShipAction(self._keyboard_service))
        self._script.add_action("output", DrawActorsAction(self._video_service))

    def _dismantle_game(self):
        self._video_service.unload_images()
        # self._sound_service.unload_sounds()

    def _add_background(self):
        self._cast.clear_actors(BACKGROUND_GROUP)
        x = 20
        y = 80
        position = Point(x, y)
        size = Point(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BACKGROUND_IMAGE)
        background = Background(body, image, True)
        self._cast.add_actor(BACKGROUND_GROUP, background)

    def _add_ship(self):
        self._cast.clear_actors(SHIP_GROUP)
        x = CENTER_X - SHIP_WIDTH / 2
        y = MAX_Y - SHIP_HEIGHT
        position = Point(x, y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(SHIP_IMAGES, SHIP_RATE)
        ship = Ship(body, animation)
        self._cast.add_actor(SHIP_GROUP, ship)