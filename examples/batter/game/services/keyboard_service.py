class KeyboardService:
    """A keyboard service inteface."""

    def is_key_down(self, key):
        """Detects if the given key is being pressed.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is being pressed; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_pressed(self, key):
        """Detects if the given key was pressed once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was pressed once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_released(self, key):
        """Detects if the given key was released once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was released once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_up(self, key):
        """Detects if the given key is released.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is released; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")