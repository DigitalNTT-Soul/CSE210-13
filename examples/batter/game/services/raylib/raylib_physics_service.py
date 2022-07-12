import pyray
from game.services.physics_service import PhysicsService 


class RaylibPhysicsService(PhysicsService):
    """ A Raylib implementation of PhysicsService."""
    def __init__(self):
        pass
        
    def has_collided(self, subject, agent):
        subject_rectangle = self._get_rectangle(subject)
        agent_rectangle = self._get_rectangle(agent)
        return pyray.check_collision_recs(subject_rectangle, agent_rectangle)

    def is_above(self, subject, agent):
        subject_rectangle = self._get_rectangle(subject)
        agent_rectangle = self._get_rectangle(agent)
        collision_rectangle = pyray.get_collision_rec(subject_rectangle, agent_rectangle)
        subject_rectangle_bottom = subject_rectangle.y + subject_rectangle.height
        collision_rectangle_bottom = collision_rectangle.y + collision_rectangle.height
        return subject_rectangle_bottom == collision_rectangle_bottom

    def is_below(self, subject, agent):
        subject_rectangle = self._get_rectangle(subject)
        agent_rectangle = self._get_rectangle(agent)
        collision_rectangle = pyray.get_collision_rec(subject_rectangle, agent_rectangle)
        subject_rectangle_top = subject_rectangle.y 
        collision_rectangle_top = collision_rectangle.y
        return subject_rectangle_top == collision_rectangle_top

    def is_left_of(self, subject, agent):
        subject_rectangle = self._get_rectangle(subject)
        agent_rectangle = self._get_rectangle(agent)
        collision_rectangle = pyray.get_collision_rec(subject_rectangle, agent_rectangle)
        subject_rectangle_right = subject_rectangle.x + subject_rectangle.width
        collision_rectangle_right = collision_rectangle.x + collision_rectangle.width
        return subject_rectangle_right == collision_rectangle_right

    def is_right_of(self, subject, agent):
        subject_rectangle = self._get_rectangle(subject)
        agent_rectangle = self._get_rectangle(agent)
        collision_rectangle = pyray.get_collision_rec(subject_rectangle, agent_rectangle)
        subject_rectangle_left = subject_rectangle.x 
        collision_rectangle_left = collision_rectangle.x
        return subject_rectangle_left == collision_rectangle_left

    def _get_rectangle(self, body):
        top = body.get_position().get_y()
        left = body.get_position().get_x()
        width = body.get_size().get_x()
        height = body.get_size().get_y()
        return pyray.Rectangle(left, top, width, height)