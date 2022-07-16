from config import *
from game.scripting.action import Action


class ControlAlienAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script):
        aliens = cast.get_actors(ALIEN_GROUP)            
        for alien in aliens:
            pass
            # alien.march_right()
            # alien.move_next()

# def execute(self, cast, script, callback):

#         aliens = cast.get_actors(ALIENS_GROUP)

#         stats = cast.get_first_actor(STATS_GROUP)
#         level = stats.get_level()

#         if level == 1:
#             time = 100

#         else:
#             time = 110 - (level * 15)
#         if time < 10:
#             time = 10
#         if self.x % time == 0:

#             for alien in aliens:
#                 body = alien.get_body()
#                 velocity = Point(0,10)
#                 position = body.get_position()
#                 position = position.add(velocity)
#                 body.set_position(position)
#         self.x += 1