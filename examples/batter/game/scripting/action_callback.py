class ActionCallback:
    """A callback that can be used to trigger scene changes."""

    def on_next(self, scene):
        """Called when we need to transition from one scene to the next.
        
        Args:
            scene: A number representing the next scene.
        """
        raise NotImplementedError("execute not implemented in base class")