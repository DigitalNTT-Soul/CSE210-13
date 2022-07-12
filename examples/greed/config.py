# simple, importable class purely intended to hold config variables

class Config:
    def __init__(self):
        self.__target_framerate = 24 # controls speed of player movement, and realistically not much else
        self.__gravity_ticks_per_second = 2
        self.__max_width = 900
        self.__max_height = 600
        self.__cell_size = 15
        self.__window_title = "Greed"
        self.__default_NPC_count = 40
        self.__jump_height = 3 # number of cells, not pixels
    
    def get_target_framerate(self):
        return self.__target_framerate

    def get_gravity_frames_per_tick(self):
        return int(self.__target_framerate / self.__gravity_ticks_per_second)
    
    def get_cell_size(self):
        return self.__cell_size

    def get_max_width(self):
        return self.__max_width

    def get_column_count(self):
        return int(self.__max_width / self.__cell_size)

    def get_max_height(self):
        return self.__max_height    
    
    def get_row_count(self):
        return int(self.__max_height / self.__cell_size)
    
    def get_window_title(self):
        return self.__window_title
    
    def get_default_NPC_count(self):
        return self.__default_NPC_count

    def get_jump_height(self):
        return self.__jump_height