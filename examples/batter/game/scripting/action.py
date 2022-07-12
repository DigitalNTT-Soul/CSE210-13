class Action:
    """A thing that is done.
    
    The responsibility of action is to do something that is important in the game. Thus, it has one
    method, execute(), which should be overridden by derived classes.
    """

    def execute(self, cast, script, callback):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        raise NotImplementedError("execute not implemented in base class")