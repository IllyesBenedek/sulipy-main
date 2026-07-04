import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 800, 400
BG_COLOR = (30, 30, 40)
ROBOT_SPEED = 4
ROBOT_HEIGHT = 120  # ekkora magasságúra kicsinyítjük a robotot
GROUND_Y = HEIGHT * 0.85  # a talajszint y-koordinátája (a háttér földje)

# A képernyő középső harmada, ahol a robot mozoghat
LEFT_BOUND = WIDTH / 3
RIGHT_BOUND = WIDTH * 2 / 3

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Háttérkép betöltése és a képernyő méretére igazítása
bg_surf = pygame.image.load("Animáció/Mozgásfázisok/img/Bg.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))

# A robot képének betöltése
robot_surf_right = pygame.image.load("Animáció/Mozgásfázisok/img/Run_1.png").convert_alpha()

# Arányos kicsinyítés ROBOT_HEIGHT magasságra
original_width, original_height = robot_surf_right.get_size()
scale_factor = ROBOT_HEIGHT / original_height
new_size = (int(original_width * scale_factor), ROBOT_HEIGHT)
robot_surf_right = pygame.transform.scale(robot_surf_right, new_size)

# A balra néző (tükrözött) változat elkészítése
robot_surf_left = pygame.transform.flip(robot_surf_right, True, False)

robot_rect = robot_surf_right.get_rect(midbottom=(LEFT_BOUND, GROUND_Y))

direction = 1  # 1 = jobbra halad, -1 = balra halad


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Irányváltás a középső harmad szélein
    if robot_rect.right >= RIGHT_BOUND:
        direction = -1
    elif robot_rect.left <= LEFT_BOUND:
        direction = 1

    robot_rect.x += ROBOT_SPEED * direction

    # A haladás irányának megfelelő kép kiválasztása
    if direction == 1:
        current_robot_surf = robot_surf_right
    else:
        current_robot_surf = robot_surf_left

    # --- Kirajzolás ---
    screen.blit(bg_surf, (0, 0))
    screen.blit(current_robot_surf, robot_rect)
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
