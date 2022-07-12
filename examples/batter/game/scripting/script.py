from game.scripting.action import Action


class Script:
    """A collection of actions."""

    def __init__(self):
        """Constructs a new Action."""
        self._actions = {}
        
    def add_action(self, group, action):
        """Adds an action to the given group.
        
        Args:
            group: A string containing the name of the group.
            action: The instance of Action to add.
        """
        if group not in self._actions.keys():
            self._actions[group] = []
        self._actions[group].append(action)

    def clear_actions(self, group):
        """Clears actions from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._actions.keys():
            self._actions[group] = []

    def clear_all_actions(self):
        """Clears all actions."""
        for group in self._actions:
            self._actions[group] = []

    def get_actions(self, group):
        """Gets the actions in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Action instances.
        """
        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results
    
    def remove_action(self, group, action):
        """Removes an action from the given group.
        
        Args:
            group: A string containing the name of the group.
            action: The instance of Action to remove.
        """
        if group in self._actions:
            self._actions[group].remove(action)