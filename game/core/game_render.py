import pygame

import game.entities.player as player
import game.entities.surface as surface
import game.consts as consts

def render(screen: pygame.Surface, 
           player: player.Player,
           platform: surface.Platform):
    player.draw(screen=screen)
    platform.draw(screen=screen)
    