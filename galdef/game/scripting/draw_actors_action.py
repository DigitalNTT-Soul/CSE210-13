from config import *
from game.casting.basics.animation import Animation
from game.casting.basics.image import Image
from game.casting.specifics.messages import Messages
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
        self._is_paused = False
        self._current_score = 0
        self._current_level = 0
        self._high_score = 0
        self._high_level = 0
        self._messages = ""
        self._game_over_message = (f"GAME  OVER!\nTO  PLAY  AGAIN  PRESS  R\nOR  PRESS  ESC  TO  EXIT  THE  GAME\n \nTHE  HIGH  SCORE  TO  BEAT  IS:    {int(self._high_score)}\n THE  HIGH  LEVEL  TO  BEAT  IS:    {int(self._high_level)}")
   
    def execute(self, cast, script, flags):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()

        self._draw_other_image_actors(cast, BACKGROUND_GROUP)
        self._draw_other_image_actors(cast, SHIP_GROUP)
        self._draw_other_image_actors(cast, SHIP_PROJECTILE_GROUP)
        self._draw_other_image_actors(cast, ALIEN_PROJECTILE_GROUP)
        self._draw_other_image_actors(cast, EXPLOSION_GROUP)
        self._draw_alien_actors(cast)
        self._draw_hud(cast)
    
        if (cast.get_actors(SHIP_GROUP) == []):
            stats = cast.get_first_actor(STATS_GROUP)

            self._messages = Messages()
            if stats.get_lives():
                pass
               
            else:
                stats = cast.get_first_actor(STATS_GROUP)
                self._current_score = stats._score
                self._current_level = stats._level
                self._messages.compare_and_store(self._current_score, self._current_level)
                self._draw_game_over_message(cast)
                self._is_paused = True
                flags.toggle_flag(PAUSE)

        self._video_service.flush_buffer()

    def _draw_hud(self, cast):
        stats = cast.get_first_actor(STATS_GROUP)
        message = cast.get_first_actor(MESSAGE_GROUP)
        self._draw_text_actor(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        self._draw_text_actor(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())
        self._draw_text_actor(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_text_actor(cast, KILLS_GROUP, KILLS_FORMAT, stats.get_kills())
        self._draw_text_actor(cast, RESTART_MESS_GROUP, RESTART_MESS_FORMAT, message.get_restart_message())
        self._draw_text_actor(cast, EXIT_MESS_GROUP, EXIT_MESS_FORMAT, message.get_exit_game_message())

    def _draw_game_over_message(self, cast):                   
        high_score_info = self._messages.retrieve_high_score() 
        self._high_score = int(high_score_info[0])
        self._high_level = int(high_score_info[1])
        game_over_message = (f"GAME  OVER!\nTO  PLAY  AGAIN  PRESS  R\nOR  PRESS  ESC  TO  EXIT  THE  GAME\n \nTHE  HIGH  SCORE  TO  BEAT  IS:    {int(high_score_info[0])}\nTHE  HIGH  LEVEL  TO  BEAT  IS:    {self._high_level}")

        self._draw_text_actor(cast, GAME_OVER_MESS_GROUP, GAME_OVER_MESS_FORMAT, game_over_message)

    def _draw_text_actor(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)
      
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

       
    def set_is_paused_true(self):
        self._is_paused = True

    def set_is_paused_false(self):
        self._is_paused = False

    def get_is_paused(self):
        return self._is_paused