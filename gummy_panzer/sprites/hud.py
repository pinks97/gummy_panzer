import pygame
import logging
LOG = logging.getLogger(__name__)

class Hud(object):

    def __init__(self, health, energy, score, time):
        self.health = health
        self.energy = energy
        self.score = score
        self.time = time
        self.surf_hp = pygame.Surface((180, 16))
        self.rect_hp = pygame.Rect(30, 0, 100, 15) 

    def draw_hud(self, surf):
        font = pygame.font.Font(None, 20)

        surfscore = font.render("Score:%d" % self.score, 1, (255, 0, 0))
        surf.blit(surfscore, (550, 0))

        surftime = font.render("Time:%d" % self.time, 1, (255, 0, 0))
        surf.blit(surftime, (400, 0))

        surfenergy = font.render("EN:%d" % self.energy, 1, (0, 255, 0))
        surf.blit(surfenergy, (200, 0))

        self.health = 85
        temp_rect = pygame.Rect(30, 0, self.health, 15)
        pygame.draw.rect(self.surf_hp, (0, 0, 255), self.rect_hp, 1)    #added test code
        pygame.draw.rect(self.surf_hp, (0, 0, 255), temp_rect, 0)
        surf.blit(self.surf_hp, (0, 0))

        surfhealth = font.render("HP:", 1, (0, 0, 255))
        surf.blit(surfhealth, (0, 0))