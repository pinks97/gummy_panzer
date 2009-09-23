# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from pygame import font
import logging
from gummy_panzer import settings
from gummy_panzer.sprites import util, effects

class ExplosionEffect(effects.SpriteSheet):

    def __init__ (self, loc,type, *groups):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = util.load_image("tractor_beam_green.png")
        if type == 'small':
            sheet = util.load_image("smallblast.png")
            image_size = (32, 32)
            self.animlen = 4
        else: 
            sheet = util.load_image("largeblast.png")
            image_size = (180, 180)
            self.animlen = 6
        effects.SpriteSheet.__init__(self, sheet, image_size, *groups)
        self.rect.width = image_size[0]
        self.rect.height = image_size[1]
        self.rect.top = loc[1]-self.rect.height/2
        self.rect.left = loc[0]-self.rect.width/2
        self.anim_frame =0
        self.draw_area = pygame.Rect((0,0),(self.rect.width,self.rect.height))
        self.drawc = 0
        self.drawcount = 2 
        
    def update (self):
         self.drawc += 1
         self.rect.left += settings.SCROLL_RATE
         if self.drawc == self.drawcount:
             self.anim_frame = (self.anim_frame + 1) % self.animlen
             self.drawc = 0
         if self.anim_frame == self.animlen-1:

             self.kill()

class PointEffect(pygame.sprite.Sprite):
    def __init__(self,loc,numpoints,size = 20,*groups):
        pygame.sprite.Sprite.__init__(self,*groups)
        self.font = pygame.font.Font(None, size)
        self.image = self.font.render("%d" % numpoints, True, (255,255,255))
        self.rect = self.image.get_rect()
       
        self.rect.top = loc[1]-self.rect.height/2-10
        self.rect.left = loc[0]-self.rect.width/2
        self.alivec = 0
        
    def update(self):
        self.rect.top-= 2
        self.alivec +=1
        if self.alivec == 20:
            self.kill()