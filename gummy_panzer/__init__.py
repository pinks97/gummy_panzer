from __future__ import absolute_import

import logging
LOG = logging.getLogger(__name__)

import pygame
from . import settings
from .sprites import player, enemies, hud

def main(argv):
    pygame.init()
    LOG.info("Starting game")
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH,
                                    settings.SCREEN_HEIGHT))
    pygame.display.set_caption('Roflmao test')
    clock = pygame.time.Clock()

    my_player = player.Player()
    TEST_ENEMY = enemies.AerialEnemy('enemy_sprite.png',300,800)
    my_hud = hud.Hud(100, 0, 0, 0)

    extra_sprites = [TEST_ENEMY]
    while True:
        clock.tick(settings.FRAMES_PER_SECOND)
        pygame.display.update()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
                elif event.key == pygame.K_SPACE:
                    my_hud.score += 5
            my_player.handle_event(event)
        else:
            extra_sprites.extend(my_player.update())
            screen.blit(my_player.image, my_player.rect.topleft)
            my_hud.draw_hud(screen)
            for sprite in extra_sprites:
                sprite.update()
                if hasattr(sprite, "draw_area"):
                    screen.blit(sprite.image, sprite.rect.topleft, sprite.draw_area)
                else:
                    screen.blit(sprite.image, sprite.rect.topleft)
            continue
        pygame.quit()
        return

__all__ = ['main']
