class Color:
    """A color."""
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red: An int between 0 and 255 representing the red value.
            green: An int between 0 and 255 representing the green value.
            blue: An int between 0 and 255 representing the blue value.
            alpha: An int between 0 and 255 representing the alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            The color as a Tuple of four values (red, green, blue, alpha)
        """
        return (self._red, self._green, self._blue, self._alpha)   