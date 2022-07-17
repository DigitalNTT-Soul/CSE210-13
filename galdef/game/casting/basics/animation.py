import time
from config import *
from game.casting.basics.image import Image

class Animation:

    def __init__(self, images, rate = 7, delay = 0):
        self._delay = delay
        self._images = images
        self._rate = rate
        self._index = 0
        self._frame = 0
        self._start = time.time()

    def get_delay(self):
        return self._delay

    def get_images(self):
        return self._images

    def get_rate(self):
        return self._rate
    
    def get_index(self):
        return self._index

    def next_image(self):
        filename = self._images[self._index]
        image = Image(filename)
        current = time.time()
        elapsed = current - self._start

        if elapsed > self._delay:
            self._frame += 1

            if self._frame >= self._rate:
                self._index = (self._index + 1) % len(self._images)
                self._frame = 0
            
            filename = self._images[self._index]
            image = Image(filename)

            if self._index >= len(self._images) - 1:
                self._start = current

        return image