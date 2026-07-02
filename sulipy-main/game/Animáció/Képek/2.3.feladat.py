import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
PLANE_SPEED = 5
PLANE_WIDTH, PLANE_HEIGHT = 120, 80

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Repülőgép")
clock = pygame.time.Clock()

bg_surf = pygame.image.load("Animáció/Képek/img/BG.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))

plane_surf = pygame.image.load("Animáció/Képek/img/Fly_1.png").convert_alpha()
plane_surf = pygame.transform.scale(plane_surf, (PLANE_WIDTH, PLANE_HEIGHT))

plane_x = 0
plane_y = 160

# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Mozgás és újrapozicionálás ---
    plane_x += PLANE_SPEED

    if plane_x > WIDTH:
        plane_x = -PLANE_WIDTH

    # --- Kirajzolás ---
    screen.blit(bg_surf, (0, 0))
    screen.blit(plane_surf, (plane_x, plane_y))
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
