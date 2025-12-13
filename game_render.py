import pygame

import player

def render(screen: pygame.Surface, 
           player: player.Player):
    player.draw(screen=screen)