class Image:

    def __init__(self, filename, scale = 1, rotation = 0):
        self._filename = filename
        self._scale = scale
        self._rotation = rotation

    def get_filename(self):
        return self._filename
    
    def get_scale(self):
        return self._scale

    def get_rotation(self):
        return self._rotation

    def set_rotation(self, rotation):
        self._rotation = rotation

    def set_scale(self, scale):
        self._scale = scale