import pygame
import Main_scripts.constants as const
from Main_scripts.constants import *
import Main_scripts.map_builder as mb
from Main_scripts.player import Player
from Main_scripts.enemy import Enemy

player = Player()

def main_loop():
    clock = pygame.time.Clock()

    win.blit(Loading_image, (100, 100))

    pygame.display.update()

    enemies = [Enemy(1, 5), Enemy(1, 5)]

    mb.build_map()

    mb.draw_map(player.pos[2])

    player.find_spawn()

    run = True

    while run:
        clock.tick(30)

        for enemy in enemies:
            if enemy.pos[2] == const.active_z:
                enemy.update()
                if player.rect.colliderect(enemy.rect) and player.frame_count == 1:
                    print("hit")
                    player.hit()
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.direction[0] = "R"
                    player.prev_direction = [player.direction[0], player.direction[1]]
                elif event.key == pygame.K_a:
                    player.direction[0] = "L"
                    player.prev_direction = [player.direction[0], player.direction[1]]
                if event.key == pygame.K_w:
                    player.direction[1] = "B"
                    player.prev_direction = [player.direction[0], player.direction[1]]
                elif event.key == pygame.K_s:
                    player.direction[1] = "F"
                    player.prev_direction = [player.direction[0], player.direction[1]]
                if event.key == pygame.K_1:
                    enemies.append(Enemy(1, player.pos[2]))

                if event.key == pygame.K_z:
                    player.shift(1)

                elif event.key == pygame.K_x:
                    player.shift(-1)
                if event.key == pygame.K_q:
                    player.place_bridge()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.direction[0] = "N"
                elif event.key == pygame.K_a:
                    player.direction[0] = "N"
                if event.key == pygame.K_w:
                    player.direction[1] = "N"
                elif event.key == pygame.K_s:
                    player.direction[1] = "N"

        update_surfaces()

        pygame.display.update()

    pygame.quit()


def update_surfaces():
    main_surface.blit(tile_map_surface, (0, 0))
    main_surface.blit(entity_surface, (0, 0))
    win.blit(main_surface, (0, 0))
    entity_surface.fill((0, 0, 0, 0))


main_loop()
