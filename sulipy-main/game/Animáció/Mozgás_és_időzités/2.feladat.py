import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 600, 300
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BG_COLOR = (127, 127, 127)

SIZE = 50


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# bal felső sarokból induló alakzat
left_x, left_y = 0, 0
left_speed_x, left_speed_y = 3, 3

# jobb felső sarokból induló alakzat
right_x, right_y = WIDTH - SIZE, 0
right_speed_x, right_speed_y = -3, 3

clock = pygame.time.Clock()


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Bal alakzat mozgása és ütközésvizsgálata ---
    left_x += left_speed_x
    left_y += left_speed_y

    if left_x <= 0 or left_x + SIZE >= WIDTH:
        left_speed_x = -left_speed_x

    if left_y <= 0 or left_y + SIZE >= HEIGHT:
        left_speed_y = -left_speed_y

    # --- Jobb alakzat mozgása és ütközésvizsgálata ---
    right_x += right_speed_x
    right_y += right_speed_y

    if right_x <= 0 or right_x + SIZE >= WIDTH:
        right_speed_x = -right_speed_x

    if right_y <= 0 or right_y + SIZE >= HEIGHT:
        right_speed_y = -right_speed_y

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)

    left_rect = pygame.Rect(left_x, left_y, SIZE, SIZE)
    right_rect = pygame.Rect(right_x, right_y, SIZE, SIZE)

    pygame.draw.rect(screen, BLUE, left_rect)
    pygame.draw.rect(screen, RED, right_rect)

    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
