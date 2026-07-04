import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
CHAR_SPEED = 5
ANIM_SPEED = 8  # ennyi ciklusonként vált mozgásfázist
CHAR_HEIGHT = 120  # ekkora magasságúra kicsinyítjük a karaktert
GROUND_Y = HEIGHT * 0.85  # a talajszint y-koordinátája (a háttér füves része)

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Háttérkép betöltése és a képernyő méretére igazítása
bg_surf = pygame.image.load("Animáció/Mozgásfázisok/img/BG.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))

# A karakter mozgásfázisai (Run_1.png - Run_8.png) betöltése ciklusban
char_surf = []
for i in range(1, 9):
    frame = pygame.image.load(f"Animáció/Mozgásfázisok/img/Run_{i}.png").convert_alpha()

    # Arányos kicsinyítés CHAR_HEIGHT magasságra
    original_width, original_height = frame.get_size()
    scale_factor = CHAR_HEIGHT / original_height
    new_size = (int(original_width * scale_factor), CHAR_HEIGHT)
    frame = pygame.transform.scale(frame, new_size)

    char_surf.append(frame)

char_index = 0
char_rect = char_surf[char_index].get_rect(bottomleft=(0, GROUND_Y))


# --- Fő ciklus ---
counter = 0
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    counter += 1
    if counter % ANIM_SPEED == 0:
        char_index += 1
    if char_index > len(char_surf) - 1:
        char_index = 0

    if char_rect.right <= WIDTH:
        char_rect.left += CHAR_SPEED

    # --- Kirajzolás ---
    screen.blit(bg_surf, (0, 0))
    screen.blit(char_surf[char_index], char_rect)
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
