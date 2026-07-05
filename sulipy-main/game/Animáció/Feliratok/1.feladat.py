import pygame
import time


# --- Beállítások ---
WIDTH, HEIGHT = 1280, 620
BG_COLOR = (140, 137, 246)

TITLE_COLOR = (255, 255, 255)
TIME_COLOR = (255, 230, 0)
SCORE_COLOR = (255, 80, 80)

# --- Inicializálás ---
pygame.init()
time_start = time.time()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Mindhárom feliratnak eltérő betűtípusa, színe és mérete van
title_font = pygame.font.SysFont("arial", 60)
time_font = pygame.font.SysFont("couriernew", 40)
score_font = pygame.font.SysFont("comicsansms", 50)

text_surf = title_font.render("GAME", True, TITLE_COLOR)
text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

score = 0


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            score += 1

    game_time = str(int(time.time() - time_start))
    time_surf = time_font.render("SEC: " + game_time, True, TIME_COLOR)
    time_rect = time_surf.get_rect(topright=(WIDTH - 10, 10))

    score_surf = score_font.render("SCORE: " + str(score), True, SCORE_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)
    screen.blit(time_surf, time_rect)
    screen.blit(score_surf, score_rect)
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    clock.tick(30)


# --- Kilépés ---
pygame.quit()
