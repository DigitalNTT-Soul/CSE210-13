from config import *
from game.casting.basics.actor import Actor


class Messages(Actor):
    """The game stats."""

    def __init__(self):
        """Constructs a new Stats."""
        super().__init__()
        self._game_over_message = "GAME  OVER!\n  TO  PLAY  AGAIN  PRESS  R\n   OR  PRESS  ESC  TO  EXIT  THE  GAME"
        self._restart_message = "PRESS  R  TO  RESTART"
        self._game_start_message = "PRESS  ENTER  TO  START"
        self._exit_game_message = "PRESS  ESC  TO  EXIT"

    def get_game_over_message(self):
        return self._game_over_message

    def get_restart_message(self):
        return self._restart_message

    def get_game_start_message(self):
        return self._game_start_message

    def get_exit_game_message(self):
        return self._exit_game_message
    