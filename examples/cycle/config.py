from game.shared.color import Color

# Now adjusts true resolution to nearest whole cell value below target resolution
TARGET_MAX_X = 900
TARGET_MAX_Y = 600
CELL_SIZE = 15
COLUMNS = int(TARGET_MAX_X / CELL_SIZE)
ROWS = int(TARGET_MAX_Y / CELL_SIZE)
MAX_X = COLUMNS * CELL_SIZE
MAX_Y = ROWS * CELL_SIZE

FONT_SIZE = CELL_SIZE

FRAME_RATE = 7
CAPTION = "CYCLE"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PLAYER_COUNT = 2