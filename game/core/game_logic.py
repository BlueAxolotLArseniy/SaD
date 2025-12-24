import game.entities.player as player
import game.entities.surface as surface

def update_logic(player: player.Player, platform: surface.Platform):
    player.update()
    
    player.collision(platform.rect_list)
    
    print(player.gravity_force, player.gravity_force_value_list)