import pygame
import time

import consts
import game_logic
import game_render
import player

def tick_calculation():
    global accumulator, last_time
    '''
    Расчет тиков для игры
    
    '''

    now = time.perf_counter()
    delta = now - last_time
    last_time = now

    accumulator += delta
    
pygame.init()
screen = pygame.display.set_mode((consts.DISPLAY_WEIGHT,
                                  consts.DISPLAY_HIGH))
clock = pygame.time.Clock()

player = player.Player(x = 600,
                       y = 100)

accumulator = 0.0
last_time = time.perf_counter()

running = True
while running:
    
    tick_calculation()

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- LOGIC (TICKS) --------
    while accumulator >= consts.TICK_TIME:
        game_logic.update_logic(player=player)
        accumulator -= consts.TICK_TIME

    # -------- RENDER --------
    
    screen.fill((0, 0, 0))
    
    game_render.render(screen=screen,
                       player=player)
    
    pygame.display.flip()

    clock.tick(480)  # FPS НЕ ОГРАНИЧИВАЕМ (или tick(144))
    


print("Finish")