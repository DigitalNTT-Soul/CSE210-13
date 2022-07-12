class MouseService:
    """A mouse service inteface."""

    def get_coordinates(self):
        """Gets the current mouse coordinates as a Point.
        
        Returns:
            Point: An instance of the batter.casting.Point class.
        """
        raise NotImplementedError("not implemented in base class")

    def has_mouse_moved(self):
        """Whether or not the mouse has moved since the last frame.
        
        Returns:
            True if the mouse moved; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_button_down(self, button):
        """Detects if the given button is pressed.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button is pressed; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_button_pressed(self, button):
        """Detects if the given button was pressed once.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button was pressed once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_button_released(self, button):
        """Detects if the given button was released once.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button was released once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_button_up(self, button):
        """Detects if the given button is released.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button is released; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")