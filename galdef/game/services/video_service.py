import pyray
from config import *
import pathlib
from game.shared.color import Color
from game.shared.os_tool import OSTool


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self):
        """Constructs a new VideoService
        """
        self._textures = {}
        self._fonts = {}

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.set_target_fps(FRAME_RATE)
        pyray.init_window(MAX_X, MAX_Y, WINDOW_TITLE)

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        # if DEBUG:
        #     self._draw_grid() # commenting out because draw_grid doesn't currently exist
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)

    def load_images(self, directory):
        filepaths = OSTool.get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                self._textures[filepath] = pyray.load_texture(filepath)
    
    def unload_images(self):
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()

    def draw_image(self, image, position):
        filepath = str(pathlib.Path(image.get_filename()))
        # fixed os dependent filepath
        texture = self._textures[filepath]
        x = position.get_x()
        y = position.get_y()
        raylib_position = pyray.Vector2(x, y)
        scale = image.get_scale()
        rotation = image.get_rotation()
        tint = self._to_raylib_color(WHITE)
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)

    def draw_rectangle(self, rectangle, color, filled = False):
        x = int(rectangle.get_position().get_x())
        y = int(rectangle.get_position().get_y())
        width = int(rectangle.get_size().get_x())
        height = int(rectangle.get_size().get_y())
        raylib_color = self._to_raylib_color(color)

        if filled:
            pyray.draw_rectangle(x, y, width, height, raylib_color)
        else:
            pyray.draw_rectangle_lines(x, y, width, height, raylib_color)
    
    def _to_raylib_color(self, color):
        r, g, b, a = color.to_tuple()
        return pyray.Color(r, g, b, a)

    def load_fonts(self, directory):
        filepaths = OSTool.get_filepaths(directory, [".otf", ".ttf"])
        for filepath in filepaths:
            if filepath not in self._fonts.keys():
                self._fonts[filepath] = pyray.load_font(filepath)

    def unload_fonts(self):
        for font in self._fonts.values():
            pyray.unload_font(font)
        self._fonts.clear()

    def draw_text(self, text, position):
        filepath = text.get_fontfile()
        filepath = str(pathlib.Path(filepath))
        value = text.get_value()
        size = text.get_size()
        spacing = 0
        alignment = text.get_alignment()
        tint = self._to_raylib_color(WHITE)
        
        font = self._fonts[filepath]
        text_image = pyray.image_text_ex(font, value, size, spacing, tint)

        x = position.get_x()
        y = position.get_y()

        if alignment == ALIGN_CENTER:
            x = (position.get_x() - text_image.width / 2)
        elif alignment == ALIGN_RIGHT:
            x = (position.get_x() - text_image.width)

        raylib_position = pyray.Vector2(x, y)
        pyray.draw_text_ex(font, value, raylib_position, size, spacing, tint)
