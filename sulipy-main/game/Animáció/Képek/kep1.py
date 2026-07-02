import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bird_surf = pygame.image.load("Animáció/Képek/img/bird1.png").convert_alpha()
bird_surf = pygame.transform.scale(bird_surf, (80, 60))
bird_x = 0
bird_y = 200


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)
    if bird_x < WIDTH - 100:
        bird_x += BIRD_SPEED
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
