import pygame

import game.consts as consts
import game.utils.loader as loader

class Player():
    def __init__(self, x: int, y: int) -> None:
        '''
        
        Главный персонаж, которым управляет пользователь
        
        :param x: положение игрока по абсциссе
        :type x: int
        :param y: положение игрока по ординате
        :type y: int
        '''
        
        self.image = loader.player_image.convert()
        self.image.set_colorkey((0, 255, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.abscissa_speed = 0
        self.friction_force = 2
        self.gravity_force = 0
        
        self.gravity_force_value_list = [0, 0, 0]
    
    def update(self):
        '''
        1. Движение игрока вправо/влево, прыжок.
        2. Сила притяжения для игрока
        3. 
        '''
        
        # -------- CONTROL --------
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.abscissa_speed -= 20
        if keys[pygame.K_d]:
            self.abscissa_speed += 20
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.gravity_force_value_list[0] < self.gravity_force_value_list[1]:
            self.gravity_force = -consts.PLAYER_JUMP_HIGH
            self.rect.y += self.gravity_force
        
        # -------- SLOW DOWN --------

        if self.abscissa_speed > 0:
            self.abscissa_speed -= self.friction_force
        if self.abscissa_speed < 0:
            self.abscissa_speed += self.friction_force
        
        # -------- SPEED LIMIT --------
        
        if self.abscissa_speed > 20:
            self.abscissa_speed = 20
        elif self.abscissa_speed < -20:
            self.abscissa_speed = -20
        
        # -------- MOVE --------
        
        self.rect.x += self.abscissa_speed
        
        # -------- FALL --------
        
        self.gravity_force += consts.GRAVITY
        self.rect.y += self.gravity_force
        
        self.gravity_force_value_list[2] = self.gravity_force_value_list[1]
        self.gravity_force_value_list[1] = self.gravity_force_value_list[0]
        self.gravity_force_value_list[0] = self.gravity_force
    
    def collision(self, list_of_objects: list):
        for object in list_of_objects:
            i = pygame.Rect(object)
            if i.colliderect(self.rect):
                self.rect.y -= self.rect.bottomright[1] - i.topright[1]
                self.gravity_force = -1


    def draw(self, screen: pygame.Surface):
        '''
        Отрисовка игрока на экране
        
        :param screen: Экран, на котором будет отрисовка
        '''
        
        screen.blit(self.image, self.rect)