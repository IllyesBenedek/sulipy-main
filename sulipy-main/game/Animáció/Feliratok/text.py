import pygame
import time

WIDTH, HEIGHT = 1280, 620
BG_COLOR = (140, 137, 246)
FONT_COLOR = (255, 255, 255)

pygame.init()
time_start = time.time()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_font = pygame.font.SysFont("arial", 60)
text_surf = game_font.render("GAME", True, FONT_COLOR)
text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            score += 1

    game_time = str(int(time.time() - time_start))
    time_surf = game_font.render("SEC: " + game_time, True, FONT_COLOR)
    time_rect = time_surf.get_rect(topright=(WIDTH - 10, 10))

    score_surf = game_font.render("SCORE: " + str(score), True, FONT_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))

    screen.fill(BG_COLOR)
    screen.blit(time_surf, time_rect)
    screen.blit(score_surf, score_rect)
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
