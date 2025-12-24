import pygame

import game.consts as consts
import game.utils.loader as loader

class Player():
    def __init__(self, x: int, y: int) -> None:
        '''
        
        Главный персонаж, которым управляет пользователь
        
        :param x: положение спавна игрока по абсциссе
        :type x: int
        :param y: положение спавна игрока по ординате
        :type y: int
        '''
        
        self.image = loader.player_image.convert()
        self.image.set_colorkey(consts.PLAYER_INVISIBLE_TEXTURE_COLOR)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * consts.PLAYER_TEXTURE_WIDTH, self.image.get_height() * consts.PLAYER_TEXTURE_HEIGHT))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.abscissa_speed = 0
        self.gravity_force = 0
        
        self.gravity_force_value_list = [0, 0, 0]
    
    def update(self) -> None:
        self.control()
        self.slow_down()
        self.speed_limit()
        
        # -------- MOVE --------
        self.rect.x += self.abscissa_speed
        
        self.fall()
        
    
    def control(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.abscissa_speed -= 20
        if keys[pygame.K_d]:
            self.abscissa_speed += 20
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.gravity_force_value_list[0] < self.gravity_force_value_list[1]:
            self.gravity_force = -consts.PLAYER_JUMP_HEIGHT
            self.rect.y += self.gravity_force
    
    def slow_down(self) -> None:
        if self.abscissa_speed > 0:
            self.abscissa_speed -= consts.PLAYER_FRICTION_FORCE
        if self.abscissa_speed < 0:
            self.abscissa_speed += consts.PLAYER_FRICTION_FORCE
    
    def collision(self, list_of_objects: list) -> None:
        for object in list_of_objects:
            i = pygame.Rect(object)
            if i.colliderect(self.rect):
                self.rect.y -= self.rect.bottomright[1] - i.topright[1]
                self.gravity_force = -1
    
    def speed_limit(self) -> None:
        if self.abscissa_speed > 20:
            self.abscissa_speed = 20
        elif self.abscissa_speed < -20:
            self.abscissa_speed = -20
    
    def fall(self) -> None:
        self.gravity_force += consts.GRAVITY
        self.rect.y += self.gravity_force
        
        self.gravity_force_value_list[2] = self.gravity_force_value_list[1]
        self.gravity_force_value_list[1] = self.gravity_force_value_list[0]
        self.gravity_force_value_list[0] = self.gravity_force

    def draw(self, screen: pygame.Surface) -> None:
        '''
        Отрисовка игрока на экране
        
        :param screen: Экран, на котором будет отрисовка
        '''
        
        screen.blit(self.image, self.rect)