class Cast:
    """A collection of actors."""

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to add.
        """
        if group not in self._actors.keys():
            self._actors[group] = []
        self._actors[group].append(actor)

    def clear_actors(self, group):
        """Clears actors from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._actors:
            self._actors[group] = []
    
    def clear_all_actors(self):
        """Clears all actors."""
        for group in self._actors:
            self._actors[group] = []
    
    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Actor instances.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            A list of actor instances.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of Actor.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)