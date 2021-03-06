from __future__ import division

import pygame
import logging
import random
import functools
from gummy_panzer.sprites import enemy_info
from gummy_panzer.sprites import damageable
from gummy_panzer.sprites import util
from gummy_panzer.sprites import effects
from gummy_panzer.sprites import weapons
from gummy_panzer import settings

LOG = logging.getLogger(__name__)

class Enemy(effects.SpriteSheet, damageable.Damageable):

    def __init__(self, sprite, loc, speed=(None, None), strength = 1,
                                                pattern = None, pat_step=0):
        self.points = 100
        if sprite == enemy_info.SPRITE_ONE:
            effects.SpriteSheet.__init__(self, util.load_image(sprite),
                                (enemy_info.STATE_W[0], enemy_info.STATE_H[0]))
            damageable.Damageable.__init__(self,
                                enemy_info.SPRITE_ONE_HEALTH * strength)
            self.bullet_v = (-weapons.MACHINE_GUN_V, 0)
            self.bullet_a = (0, 0)
            if speed[0] == None:
                self.speedx = 1
            else:
                self.speedx = speed[0]
            if speed[1] == None:
                self.speedy = 6
            else:
                self.speedy = speed[1]
            #self.points = 
            if pattern == None:
                self.pattern = enemy_info.PATTERN_STRAIGHT
            else:
                self.pattern = pattern

        elif sprite == enemy_info.SPRITE_TWO:
            effects.SpriteSheet.__init__(self, util.load_image(sprite),
                                (enemy_info.STATE_W[0], enemy_info.STATE_H[0]))
            damageable.Damageable.__init__(self,
                                enemy_info.SPRITE_TWO_HEALTH * strength)
            self.bullet_v = (-weapons.MACHINE_GUN_V, 0)
            self.bullet_a = (0, 0)
            if speed[0] == None:
                self.speedx = 3
            else:
                self.speedx = speed[0]
            if speed[1] == None:
                self.speedy = 4
            else:
                self.speedy = speed[1]
            #self.points =
            if pattern == None:
                self.pattern = enemy_info.PATTERN_CIRCLE_BOTTOM
            else:
                self.pattern = pattern

        elif sprite == enemy_info.SPRITE_THREE:
            effects.SpriteSheet.__init__(self, util.load_image(sprite),
                                (enemy_info.STATE_W[2], enemy_info.STATE_H[2]))
            damageable.Damageable.__init__(self,
                                enemy_info.SPRITE_THREE_HEALTH * strength)
            self.bullet_v = (-(weapons.MACHINE_GUN_V * 4) / 5,
                                -(weapons.MACHINE_GUN_V * 3) / 5)
            self.bullet_a = (-0.2, 0.1)
            self.speedx = self.speedy = 0
            self.strength = 1
            #self.points =
            self.pattern = enemy_info.PATTERN_DIAG_UP
        else:
            self.speed = 0
            self.strength = 1
            self.pattern = enemy_info.PATTERN_DIAG_DOWN

        LOG.debug("spam " + unicode(self.rect))
        self.rect.topleft = loc
        LOG.debug("eggs " + unicode(self.rect))

        self.e_state = enemy_info.STATE_MOVING
        self.pat_step = pat_step
        self.anim_update_counter = 0
        self.anim_frame = 0
        self.falling = False
        self.last_speed_x = 0
        self.last_speed_y = 0

        self.accel_counter_x = 0
        self.accel_coFunter_y = 0

        self._gun_factory = weapons.WeaponFactory(40,
                functools.partial(weapons.MachineGun, charge=2))

    
    def update(self):

        self.anim_update_counter+=1

        if (self.e_state == enemy_info.STATE_MOVING or
                            self.e_state == enemy_info.STATE_SHOOTING):
            self.last_speed_x =((self.speedx * self.pattern[self.pat_step][0]) +
                                                        settings.SCROLL_RATE)
            self.last_speed_y = (self.speedy * self.pattern[self.pat_step][1])
            self.rect.left += self.last_speed_x
            self.rect.top += self.last_speed_y

            self.pat_step+=1
            if self.pat_step == len(self.pattern):
                self.pat_step = 0

            bullets = []
            if self._gun_factory.can_fire():
                bullets.append(self._gun_factory.fire())
            bullets = filter(lambda x: x is not None, bullets)
            assert all(bullets)

            for bullet in bullets:
                bullet.rect.centery = self.rect.centery
                bullet.rect.right = self.rect.left
                bullet.velocity = self.bullet_v
                bullet.acceleration = self.bullet_a
                bullet.image = pygame.transform.flip(bullet.image, True, False)
            self._gun_factory.tick()
            return bullets

        elif self.e_state == enemy_info.STATE_DYING:
            self.rect.left += self.last_speed_x
            self.rect.top += self.last_speed_y

            

            self.accel_counter_x += 1
            if self.accel_counter_x == 3 and self.last_speed_x != \
                                                    settings.SCROLL_RATE:
                self.last_speed_x -= 1
            self.last_speed_y += 1
            return tuple()

        if (self.anim_update_counter ==
                    (enemy_info.ANIMATION_FRAMES[self.e_state])[self.anim_frame]):
                self.anim_frame += 1
                if (self.anim_frame ==
                                len(enemy_info.ANIMATION_FRAMES[self.e_state])):
                    self.anim_frame = 0








        #return projectiles if shooting

    def dying(self):
        self.e_state = enemy_info.STATE_DYING

            
