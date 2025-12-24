import pygame
import time

import game.utils.math as math_methods
import game.consts as consts
import game.core.game_logic as game_logic
import game.core.game_render as game_render
import game.entities.player as player
import game.entities.surface as surface

pygame.init()

class Game():
    def __init__(self):
        self.is_main_cycle_working = True
        
        self.platform = surface.Platform([(600, 400,200, 20),
                                          (100, 200,200, 20)])
        
        self.player = player.Player(x = 600,
                       y = 100)

        self.screen = pygame.display.set_mode((consts.DISPLAY_WEIGHT,
                                        consts.DISPLAY_HIGH))
        
        pygame.display.set_caption("Stay and Die")
        self.clock = pygame.time.Clock()

        self.now = 0.0
        self.delta = 0.0
        self.accumulator = 0.0
        self.last_time = time.perf_counter()

        
    def run(self):
        while self.is_main_cycle_working:
    
            math_methods.tick_calculation(self.now, self.delta, self.last_time, self.accumulator)

            # -------- EVENTS --------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # -------- LOGIC (TICKS) --------
            while self.accumulator >= consts.TICK_TIME:
                game_logic.update_logic(player=self.player,
                                        platform=self.platform)
                self.accumulator -= consts.TICK_TIME

            # -------- RENDER --------
            
            self.screen.fill((0, 0, 0))
            
            game_render.render(screen = self.screen,
                            player = self.player,
                            platform = self.platform)
            
            pygame.display.flip()

            self.clock.tick(144)  # F