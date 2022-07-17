from game.casting.basics.actor import Actor


class Explosion(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation):
        """Constructs a new Explosion.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
        """
        super().__init__()
        self._body = body
        self._animation = animation
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
