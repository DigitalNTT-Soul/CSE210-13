from config import *
from game.scripting.action import Action
from game.shared.point import Point


class MoveAlienAction(Action):

    def __init__(self):
        self._movement_phase = 0 # 0 for moving right, 1 for left, 2 for forward-then-left, 3 for forward-then-right
        self._left_bound = 0
        self._right_bound = MAX_X
        self._bottom_bound = MAX_Y - SHIP_HEIGHT
        self._collision_velocity = Point()
        
    def execute(self, cast, script, flags):
        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        if alien_grid == []:
            self._movement_phase = 0
            return
        
        vanguard_alien = alien_grid[-1][0]
        grid_bottom = vanguard_alien.get_body().get_bottom()
        horizontal_speed = vanguard_alien.get_level_speed()
        vertical_speed = vanguard_alien.get_height()
        grid_on_floor = (grid_bottom == self._bottom_bound)

        match self._movement_phase:
            case 0: # moving right, so check right edge and wall
                for row in alien_grid:
                    row_right_edge = row[-1].get_body().get_right()
                    if row_right_edge + horizontal_speed > self._right_bound:
                        gap_width = self._right_bound - row_right_edge
                        new_velocity = Point(gap_width, 0)
                        self._marching_orders(alien_grid, new_velocity)
                        if grid_on_floor:
                            self._movement_phase = 1 # move grid left next frame
                        else:
                            self._movement_phase = 2 # move grid forward next frame
                        return
                # this only executes if the loop ends without any row being too close to the wall
                self._marching_orders(alien_grid, "right") # ensure we move at alien._level_speed
            case 1: # moving left, so check left edge and wall
                for row in alien_grid:
                    row_left_edge = row[0].get_body().get_left()
                    if row_left_edge - horizontal_speed < self._left_bound:
                        gap_width = self._left_bound - row_left_edge
                        new_velocity = Point(gap_width, 0)
                        self._marching_orders(alien_grid, new_velocity)
                        if grid_on_floor:
                            self._movement_phase = 0 # move grid right next frame
                        else:
                            self._movement_phase = 3 # move grid forward next frame
                        return
                # this only execute if the loop ends without any row being too close to the wall
                self._marching_orders(alien_grid, "left") # ensure we move at alien._level_speed
            case 2:
                if grid_bottom + vertical_speed > self._bottom_bound: # have to get level_speed because grid should have no vertical velocity at this point
                    gap_width = self._bottom_bound - grid_bottom
                    new_velocity = Point(0, gap_width)
                    self._marching_orders(alien_grid, new_velocity)
                else:
                    self._marching_orders(alien_grid, "forward")
                self._movement_phase = 1
            case 3:
                if grid_bottom + vertical_speed > self._bottom_bound: # have to get level_speed because grid should have no vertical velocity at this point
                    gap_width = self._bottom_bound - grid_bottom
                    new_velocity = Point(0, gap_width)
                    self._marching_orders(alien_grid, new_velocity)
                else:
                    self._marching_orders(alien_grid, "forward")
                self._movement_phase = 0

    def _marching_orders(self, grid, velocity):
        for row in grid:
            for alien in row:
                if isinstance(velocity, Point):
                    alien.set_specific_velocity(velocity)
                elif isinstance(velocity, str):
                    match velocity:
                        case "left":
                            alien.march_left()
                        case "right":
                            alien.march_right()
                        case "forward":
                            alien.march_forward()