class Sound:
    def __init__(self, filename, volume = 1, repeated = False):
        self._filename = filename
        self._volume = volume
        self._repeated = repeated

    def get_filename(self):
        return self._filename

    def get_volume(self):
        return self._volume

    def set_volume(self, volume_num):
        self._volume = volume_num

    def is_repeated(self):
        return self._repeated