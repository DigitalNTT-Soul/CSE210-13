
from config import *
from random import randint

from game.casting.basics.cast import Cast
from game.casting.basics.body import Body
from game.casting.basics.image import Image
from game.casting.basics.sound import Sound
from game.casting.basics.animation import Animation
from game.casting.basics.text import Text
from game.casting.basics.label import Label

from game.casting.specifics.ship import Ship
from game.casting.specifics.alien import Alien
from game.casting.specifics.background import Background
from game.casting.specifics.stats import Stats
from game.casting.specifics.messages import Messages

from game.scripting.script import Script
from game.scripting.move_alien_action import MoveAlienAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.mute_unmute_action import MuteUnmuteAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.control_ship_action import ControlShipAction
from game.scripting.prune_explosions_action import PruneExplosionsAction
from game.scripting.prune_missed_shots_action import PruneMissedShotsAction
from game.scripting.bullet_collide_ship_action import BulletCollideShipAction
from game.scripting.bullet_collide_alien_action import BulletCollideAlienAction
from game.scripting.bullet_collide_bullet_action import BulletCollideBulletAction
from game.scripting.alien_fire_projectile_action import AlienFireProjectileAction
from game.scripting.player_fire_projectile_action import PlayerFireProjectileAction
from game.scripting.toggle_hardcore_mode_action import ToggleHardcoreModeAction
from game.scripting.increase_decrease_volume_action import IncreaseDecreaseVolumeAction
from game.scripting.pause_action import PauseAction

from game.services.video_service import VideoService
from game.services.sound_service import SoundService
from game.services.keyboard_service import KeyboardService
from game.services.physics_service import PhysicsService

from game.shared.point import Point
from game.shared.flags import Flags

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = KeyboardService()
        self._video_service = VideoService()
        self._sound_service = SoundService()
        self._physics_service = PhysicsService()
        self._cast = Cast() 
        self._script = Script()
        self._flags = Flags()
        self._play_new_round = True
               

    def start_game(self):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        # while self._play_new_round:
        self._build_game()
        self._sound_service.play_sound(GAME_THEME)

        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            if not self._flags.get_flag(PAUSE):
                self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)

            if not self._sound_service.is_sound_playing(GAME_THEME):
                self._sound_service.play_sound(GAME_THEME)
            if (self._cast.get_first_actor(ALIEN_GROUP) == []):
                stats = self._cast.get_first_actor(STATS_GROUP)
                stats.next_level()
                stats.add_life()
                self._add_alien_grid()
                self._add_background()

            if (self._cast.get_actors(SHIP_GROUP) == []):
                stats = self._cast.get_first_actor(STATS_GROUP)
                if stats.get_lives():
                    self._add_ship()
                    stats.lose_life()
                else:
                    self._reset_game()

            if self._keyboard_service.is_key_pressed('r'):
                self._reset_game()
            

        self._video_service.close_window()

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self._flags)

    def _build_game(self):
        """ Builds the game
        """

        self._flags.set_flag(HARDCORE, False)
        self._flags.set_flag(PAUSE, False)
        self._video_service.load_images("galdef/assets/images")
        self._video_service.load_images("galdef/assets/images/backgrounds")
        self._video_service.load_fonts("galdef/assets/fonts")
        self._sound_service.initialize()
        self._sound_service.load_sounds("galdef/assets/sounds")
        self._add_background()
        self._add_all_stats()
        self._add_all_messages()
        self._add_ship()
        self._add_alien_grid()
        

        # Come up with input, update, and output actions to script
        self._script.add_action(INPUT, ControlShipAction(self._keyboard_service))
        self._script.add_action(INPUT, MuteUnmuteAction(self._keyboard_service, self._sound_service))
        self._script.add_action(INPUT, IncreaseDecreaseVolumeAction(self._keyboard_service, self._sound_service))
        self._script.add_action(INPUT, PlayerFireProjectileAction(self._keyboard_service, self._sound_service))
        self._script.add_action(INPUT, ToggleHardcoreModeAction(self._keyboard_service))
        self._script.add_action(INPUT, PauseAction(self._keyboard_service))
        self._script.add_action(UPDATE, AlienFireProjectileAction(self._sound_service))
        self._script.add_action(UPDATE, BulletCollideAlienAction(self._physics_service, self._sound_service))
        self._script.add_action(UPDATE, BulletCollideShipAction(self._physics_service,self._sound_service))
        self._script.add_action(UPDATE, BulletCollideBulletAction(self._physics_service,self._sound_service))
        self._script.add_action(UPDATE, MoveAlienAction())
        self._script.add_action(UPDATE, MoveActorsAction())
        self._script.add_action(UPDATE, PruneExplosionsAction())
        self._script.add_action(UPDATE, PruneMissedShotsAction())
        self._script.add_action(OUTPUT, DrawActorsAction(self._video_service))
        
    def _reset_game(self):
        self._cast.clear_actors(ALIEN_PROJECTILE_GROUP)
        self._cast.clear_actors(SHIP_PROJECTILE_GROUP)
        self._add_background()
        self._add_all_stats()
        self._add_ship()
        self._add_alien_grid()

    def _dismantle_game(self):
        self._cast.clear_all_actors()
        self._video_service.unload_images()
        self._sound_service.unload_sounds()
        self._sound_service.release()
        self._video_service.unload_fonts()

    def _add_background(self):
        self._cast.clear_actors(BACKGROUND_GROUP)
        position = Point()
        velocity = Point()
        size = Point(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
        body = Body(position, size, velocity)
        image_num = randint(0, len(BACKGROUND_IMAGES)-1)
        image = Image(BACKGROUND_IMAGES[image_num])
        background = Background(body, image)
        self._cast.add_actor(BACKGROUND_GROUP, background)

    def _add_ship(self):
        self._cast.clear_actors(SHIP_GROUP)
        x = CENTER_X - SHIP_WIDTH / 2
        y = MAX_Y - SHIP_HEIGHT
        position = Point(x, y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(SHIP_IMAGE)
        ship = Ship(body, image)
        self._cast.add_actor(SHIP_GROUP, ship)

    def _add_alien(self, column, row):
        x = column * ALIEN_WIDTH
        y = row * ALIEN_HEIGHT
        position = Point(x, y)
        size = Point(ALIEN_WIDTH, ALIEN_HEIGHT)
        velocity = Point()
        body = Body(position, size, velocity)
        # image = Image(ALIEN_IMAGES["b"])
        alien_img_num = randint(0, len(ALIEN_IMAGES) - 1)
        animation = Animation(ALIEN_IMAGES[alien_img_num], ALIEN_RATE, ALIEN_DELAY)
        level = self._cast.get_first_actor(STATS_GROUP).get_level()
        alien = Alien(body, animation, level, self._flags)
        alien.march_right()
        # self._cast.add_actor(ALIEN_GROUP, alien)
        return alien
        
    def _add_all_stats(self):
        self._cast.clear_actors(STATS_GROUP)
        self._cast.clear_actors(MESSAGE_GROUP)
        self._cast.add_actor(STATS_GROUP, Stats(self._flags))
        self._cast.add_actor(MESSAGE_GROUP, Messages())
        
        position = Point(HUD_MARGIN, HUD_MARGIN)
        self._add_stat(LEVEL_GROUP, LEVEL_FORMAT, ALIGN_LEFT, position)
        position = Point(2 * (MAX_X/3), HUD_MARGIN)
        self._add_stat(KILLS_GROUP, KILLS_FORMAT, ALIGN_CENTER, position)
        position = Point((MAX_X/3), HUD_MARGIN)
        self._add_stat(SCORE_GROUP, SCORE_FORMAT, ALIGN_CENTER, position)
        position = Point(MAX_X - HUD_MARGIN, HUD_MARGIN)
        self._add_stat(LIVES_GROUP, LIVES_FORMAT, ALIGN_RIGHT, position)

    def _add_all_messages(self):
        position = Point(HUD_MARGIN, MAX_Y - (HUD_MARGIN))
        self._add_message(RESTART_MESS_GROUP, RESTART_MESS_FORMAT, ALIGN_LEFT, position)
        position = Point(MAX_X + 40, MAX_Y - (HUD_MARGIN))
        self._add_message(EXIT_MESS_GROUP, EXIT_MESS_FORMAT, ALIGN_CENTER, position)
        

    def _add_stat(self, group, format, alignment, position):
        self._cast.clear_actors(group)
        text = Text(format, FONT_FILE, FONT_SMALL, alignment)
        label = Label(text, position)
        self._cast.add_actor(group, label)

    def _add_message(self, group, format, alignment, position):
        self._cast.clear_actors(group)
        text = Text(format, FONT_FILE, 10, alignment)
        label = Label(text, position)
        self._cast.add_actor(group, label)
        
    def _add_alien_grid(self):
        self._cast.clear_actors(ALIEN_GROUP)
        alien_grid = []
        for i in range(ALIEN_GRID_ROWS):
            alien_grid.append([])
            for j in range(ALIEN_GRID_COLUMNS):
                alien = self._add_alien(j, i)
                alien_grid[i].append(alien)
        self._cast.add_actor(ALIEN_GROUP, alien_grid)