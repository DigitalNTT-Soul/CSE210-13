from constants import * 


class Text:
    """A text message."""

    def __init__(self, value, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_LEFT):
        """Constructs a new Text."""
        self._value = value
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment

    def get_alignment(self):
        """Gets the alignment for the text.
        
        Returns:
            A number representing the text alignment.
        """
        return self._alignment

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

    def get_value(self):
        """Gets the text's value.
        
        Returns:
            A string containing the text's value.
        """
        return self._value

    def set_value(self, value):
        """Sets the text's value.
        
        Args:
            A string containing the text's value.
        """
        self._value = value