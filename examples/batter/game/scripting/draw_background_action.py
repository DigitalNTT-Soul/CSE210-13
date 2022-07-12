from constants import *
from game.scripting.action import Action


class DrawBackgroundAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        background = cast.get_actors(BACKGROUND_GROUP)
        
        for bg in background:
            body = bg.get_body()

            if bg.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = bg.get_animation()
            position = body.get_position()
            self._video_service.draw_image(animation, position)