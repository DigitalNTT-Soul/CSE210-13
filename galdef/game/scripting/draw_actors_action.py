from config import *
from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()

        # scores = cast.get_actors("scores")
        # for score in scores:
        #     self._video_service.draw_actor(score)

        # cycles = cast.get_actors("cycles")
        # for cycle in cycles:
        #     self._video_service.draw_actors(cycle.get_segments())

        # messages = cast.get_actors("messages")
        # self._video_service.draw_actors(messages, True)

        self._draw_text_actors(cast, script)
        self._draw_image_actors(cast, script)
        
        self._video_service.flush_buffer()

    def _draw_text_actors(self, cast, script):
        pass
        # level = cast.get_first_actor(LEVEL_GROUP)
        # lives = cast.get_first_actor(LIVES_GROUP)
        # score = cast.get_first_actor(SCORE_GROUP)

        # self._video_service.draw_text_actor(level)
        # self._video_service.draw_text_actor(lives)
        # self._video_service.draw_text_actor(score)

    def _draw_image_actors(self, cast, script):
        ships = cast.get_actors(SHIP_GROUP)
        for ship in ships: # should only be one
            position = ship.get_body().get_position()
            image = ship.get_animation().next_image()
            self._video_service.draw_image(image, position)

        aliens = cast.get_actors(ALIEN_GROUP)
        for alien in aliens:
            position = alien.get_body().get_position()
            image = alien.get_animation().next_image()
            self._video_service.draw_image(image, position)

        projectiles = cast.get_actors(PROJECTILE_GROUP)
        for projectile in projectiles:
            position = projectile.get_body().get_position()
            image = projectile.get_animation().next_image()
            self._video_service.draw_image(image, position)
