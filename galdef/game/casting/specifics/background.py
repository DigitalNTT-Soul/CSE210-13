from game.casting.basics.actor import Actor

class Background(Actor):
    def __init__(self, body, animation):
        super().__init__()
        self._body = body
        self._animation = animation

    def get_animation(self):
        return self._animation
    
    def get_body(self):
        return self._body