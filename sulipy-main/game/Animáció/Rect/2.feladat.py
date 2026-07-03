import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
PLANE_SPEED = 5

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

plane_surf = pygame.image.load("Animáció/Rect/img/Fly_1.png").convert_alpha()
plane_surf_flipped = pygame.image.load("Animáció/Rect/img/Fly_1_back.png").convert_alpha()
plane_rect = plane_surf.get_rect(midleft=(0, HEIGHT / 2))
plane_forward = True


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)

    if plane_forward:
        plane_rect.left += PLANE_SPEED
        if plane_rect.right >= WIDTH:
            plane_forward = False
    else:
        plane_rect.left -= PLANE_SPEED
        if plane_rect.left <= 0:
            plane_forward = True

    current_surf = plane_surf if plane_forward else plane_surf_flipped
    screen.blit(current_surf, plane_rect)
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
