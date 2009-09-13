import pygame
from . import util

ACCEL = 2
MAX_V = 10

class _MovingState(object):
    STOPPED = 0
    PLUS = 1
    MINUS = -1

class Player(pygame.sprite.Sprite):

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = util.load_image("player.png")
        self.rect = self.image.get_rect()
        self._ms_x = _MovingState.STOPPED
        self._ms_y = _MovingState.STOPPED
        class _Velocity(object):
            x = 0
            y = 0
        self._velocity = _Velocity()

    def move_up(self):
        self._ms_y = _MovingState.MINUS

    def move_down(self):
        self._ms_y = _MovingState.PLUS

    def move_left(self):
        self._ms_x = _MovingState.MINUS

    def move_right(self):
        self._ms_x = _MovingState.PLUS

    @staticmethod
    def _get_physics(current_position, current_velocity, moving_state):
        """Returns (new velocity, new x)"""

        if moving_state == _MovingState.STOPPED:
            if current_velocity > 0:
                acceleration = -ACCEL
            elif current_velocity < 0:
                acceleration = ACCEL
            else:
                acceleration = 0
        elif moving_state == _MovingState.PLUS:
            acceleration = ACCEL
        else:
            acceleration = -ACCEL

        current_position += current_velocity
        velocity = min(MAX_V, current_velocity + acceleration)
        velocity = max(-MAX_V, velocity + acceleration)
        if (moving_state == _MovingState.STOPPED and
                (velocity > 0 and current_velocity < 0 ) or
                (velocity < 0 and current_velocity > 0)):
            velocity = 0
        return (velocity, current_position)

    def update(self):
        x, y = self.rect.topleft

        self._velocity.x, x = Player._get_physics(x,
                                                  self._velocity.x,
                                                  self._ms_x)
        self._velocity.y, y = Player._get_physics(y,
                                                  self._velocity.y,
                                                  self._ms_y)

        self._ms_x = _MovingState.STOPPED
        self._ms_y = _MovingState.STOPPED
        self.rect.topleft = x, y