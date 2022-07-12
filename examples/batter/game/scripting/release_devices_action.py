from game.scripting.action import Action


class ReleaseDevicesAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.release()
        self._video_service.release()