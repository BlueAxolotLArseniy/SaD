import pygame

import consts

class Player():
    def __init__(self, x: int, y: int):
        '''
        :param x: положение игрока по абциссе
        :type x: int
        :param y: положение игрока по ординате
        :type y: int
        '''
        
        self.image = pygame.image.load('textures/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.x = x
        self.y = y
        self.gravity_force = 0
    
    def update(self):
        '''
        1. Движение игрока вправо/влево, прыжок.
        2. Сила притяжения для игрока
        3. 
        '''
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= consts.PLAYER_SPEED_PER_TICK
        if keys[pygame.K_d]:
            self.x += consts.PLAYER_SPEED_PER_TICK
        if keys[pygame.K_w]:
            self.y -= consts.PLAYER_JUMP_HIGH
            
        self.gravity_force += 1
        self.y += self.gravity_force

    def draw(self, screen: pygame.Surface):
        '''
        Отрисовка игрока на экране
        
        :param screen: Экран, на котором будет отрисовка
        '''
        
        screen.blit(self.image, self.rect)