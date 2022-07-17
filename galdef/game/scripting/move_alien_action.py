from config import *
from game.scripting.action import Action
from game.shared.point import Point


class MoveAlienAction(Action):

    def __init__(self):
        self._grid_colliding_left = False
        self._grid_colliding_right = False
        self._grid_against_left = False
        self._grid_against_right = False
        self._collision_velocity = Point()
        self._next_march = "right"
        pass
        
    def execute(self, cast, script):
        alien_grid = cast.get_first_actor(ALIEN_GROUP)

        # loop through rows to check just for wall collisions
        for row in alien_grid:
            left_alien_current_x = row[0].get_body().get_position().get_x()
            right_alien_current_x = row[-1].get_body().get_position().get_x()
            current_grid_x_velocity = row[0].get_body().get_velocity().get_x()
            if (left_alien_current_x + current_grid_x_velocity) < 0:
                self._grid_colliding_left = True
                break
            if (right_alien_current_x + current_grid_x_velocity) > (MAX_X - ALIEN_WIDTH):
                self._grid_colliding_right = True
                break
        
        # march_forward and reset collision booleans if the grid is against a wall.
        if (self._grid_colliding_left):
            self._marching_orders(alien_grid, "forward")
            self._grid_colliding_left = False
            self._grid_against_left = True
        elif (self._grid_colliding_right):
            self._marching_orders(alien_grid, "forward")
            self._grid_colliding_right = False
            self._grid_against_right = True

        # march_right if against left wall and not colliding this frame
        elif self._grid_against_left and not self._grid_colliding_left:
            self._marching_orders(alien_grid, "right")
            self._grid_against_left = False

        # march_left if against right wall and not colliding this frame
        elif self._grid_against_right and not self._grid_colliding_right:
            self._marching_orders(alien_grid, "left")
            self._grid_against_right = False

    def _marching_orders(self, grid, direction):
        for row in grid:
            for alien in row:
                match direction:
                    case "left":
                        alien.march_left()
                    case "right":
                        alien.march_right()
                    case "forward":
                        alien.march_forward()