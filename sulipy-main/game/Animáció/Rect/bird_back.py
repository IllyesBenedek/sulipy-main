import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_surf = pygame.image.load("Animáció/Rect/img/bird1.png").convert_alpha()
bird_rect = bird_surf.get_rect(midleft=(0, HEIGHT / 2))
bird_forward = True


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)

    if bird_rect.right < WIDTH and bird_forward:
        bird_rect.left += BIRD_SPEED
    elif bird_rect.right == WIDTH:
        bird_forward = False
        bird_surf = pygame.image.load("Animáció/Rect/img/bird1back.png").convert_alpha()
        bird_rect = bird_surf.get_rect(midright=(WIDTH - 1, HEIGHT / 2))
    else:
        bird_rect.left -= BIRD_SPEED
    screen.blit(bird_surf, bird_rect)
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
