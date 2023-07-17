from sys import exit
import pygame

FRAME_RATE = 60

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('some game')

clock = pygame.time.Clock()

pixel_font = pygame.font.Font('font/Pixeltype.ttf', 35)

sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(30, 300))

i = 0
score = 0
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(pygame.mouse.get_pos()):
            if player_rect.bottom >= 300:
                player_gravity = -20
                print('mouse on player and pressed')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom >= 300:
                    player_gravity = -20
                    print('jump')

    i += 1
    if i % FRAME_RATE == 0:
        score += 1

    score_surf = pixel_font.render(f'Your score: {score}', False, 'Black').convert_alpha()

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(score_surf, (20, 20))

    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    snail_rect.left -= 10

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    player_gravity += 1
    player_rect.bottom += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        loosing_surface = pixel_font.render(f'You lose! Your final score is {score}', False, 'Red').convert_alpha()
        screen.blit(loosing_surface, loosing_surface.get_rect(center=(400, 200)))

        restart_surface = pixel_font.render('RESTART', False, 'Black').convert_alpha()
        restart_rect = restart_surface.get_rect(center=(400, 100))
        screen.blit(restart_surface, restart_rect)

        pygame.display.update()

        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(pygame.mouse.get_pos()):
                    snail_rect.left = 800
                    score = 0
                    i = 0
                    restart = True

    pygame.display.update()
    clock.tick(FRAME_RATE)
