from config import *
from game.casting.basics.animation import Animation
from game.casting.basics.image import Image
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
        self._draw_other_image_actors(cast, BACKGROUND_GROUP)
        self._draw_other_image_actors(cast, SHIP_GROUP)
        self._draw_other_image_actors(cast, PROJECTILE_GROUP)
        self._draw_alien_actors(cast)

        
        self._video_service.flush_buffer()

    def _draw_text_actors(self, cast, script):
        pass
        # level = cast.get_first_actor(LEVEL_GROUP)
        # lives = cast.get_first_actor(LIVES_GROUP)
        # score = cast.get_first_actor(SCORE_GROUP)

        # self._video_service.draw_text_actor(level)
        # self._video_service.draw_text_actor(lives)
        # self._video_service.draw_text_actor(score)

    def _draw_other_image_actors(self, cast, group):
        actors = cast.get_actors(group)
        for actor in actors:
            self._draw_an_image_actor(actor)
    
    def _draw_alien_actors(self, cast):
        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        for row in alien_grid:
            for alien in row:
                self._draw_an_image_actor(alien)

    def _draw_an_image_actor(self, actor):
        position = actor.get_body().get_position()
        animation = actor.get_animation()

        if isinstance(animation, Animation):
            image = animation.next_image()
        elif isinstance(animation, Image):
            image = animation
        self._video_service.draw_image(image, position)

        if DEBUG:
            rectangle = actor.get_body().get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)