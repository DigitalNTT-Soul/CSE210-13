from constants import *
from game.scripting.action import Action


class MoveBallAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
