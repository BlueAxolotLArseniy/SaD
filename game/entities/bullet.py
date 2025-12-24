import pygame

class Bullet():
    def __init__(self):
        self.rect_list = rect_list
    
    def draw(self, screen: pygame.Surface):
        for rect in self.rect_list:
            pygame.draw.rect(screen, (0, 255, 0), rect)
        