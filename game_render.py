import pygame

import player
import surface

def render(screen: pygame.Surface, 
           player: player.Player,
           platform: surface.Platform):
    player.draw(screen=screen)
    platform.draw(screen=screen)
    