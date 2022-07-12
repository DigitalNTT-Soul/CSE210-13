from game.scripting.action import Action


class StartDrawingAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        self._video_service.clear_buffer()