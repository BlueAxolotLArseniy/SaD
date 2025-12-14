import player
import surface

def update_logic(player: player.Player, platform: surface.Platform):
    player.update()
    
    player.collision(platform.rect_list)
    