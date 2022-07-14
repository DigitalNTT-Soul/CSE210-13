MAX_X = 1040
MAX_Y = 680
CENTER_X = int(MAX_X / 2)
CENTER_Y = int(MAX_Y / 2)

FRAME_RATE = 60
WINDOW_TITLE = "Galaxy Defenders"

#SOUNDS
WIL = "galdef/assets/sounds/wilhelmscream.mp3"

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 100
MAXIMUM_LIVES = 100

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# PROJECTILE
PROJECTILE_GROUP = "PROJECTILEs".lower()
PROJECTILE_IMAGE = "galdef/assets/images/000.png"
PROJECTILE_WIDTH = 28
PROJECTILE_HEIGHT = 28
PROJECTILE_VELOCITY = 6

# BACKGROUND
BACKGROUND_GROUP = "Background".lower()
BACKGROUND_WIDTH = "1040"
BACKGROUND_HEIGHT = "680"
BACKGROUND_IMAGES = [
    "galdef/assets/images/backgrounds/dark_city.png",
    "galdef/assets/images/backgrounds/clif.png",
    "galdef/assets/images/backgrounds/future_city.png",
    "galdef/assets/images/backgrounds/green_hill.png",
    'galdef/assets/images/backgrounds/cosmic_cliffs_background.png'
]

# SHIP
SHIP_GROUP = "ships".lower()
SHIP_IMAGES = [f"galdef/assets/images/{n:03}.png" for n in range(100, 103)]
SHIP_WIDTH = 100
SHIP_HEIGHT = 100
SHIP_RATE = 6
SHIP_VELOCITY = 7

# ALIEN
ALIEN_GROUP = "aliens".lower()
ALIEN_IMAGES = {
    "b": [f"galdef/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"galdef/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"galdef/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"galdef/assets/images/{i:03}.png" for i in range(40,49)]
}
ALIEN_WIDTH = 80
ALIEN_HEIGHT = 28
ALIEN_DELAY = 0.5
ALIEN_RATE = 4

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
MUTE = "m"