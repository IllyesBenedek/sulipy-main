import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 600, 300
BLUE = (0, 0, 255)
BG_COLOR = (127, 127, 127)

RECT_WIDTH, RECT_HEIGHT = 100, 50


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rect_pos_x = 10
rect_pos_y = 20
speed_x = 5
speed_y = 2

clock = pygame.time.Clock()


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Mozgás és ütközésvizsgálat ---
    rect_pos_x += speed_x
    rect_pos_y += speed_y

    if rect_pos_x <= 0 or rect_pos_x + RECT_WIDTH >= WIDTH:
        speed_x = -speed_x

    if rect_pos_y <= 0 or rect_pos_y + RECT_HEIGHT >= HEIGHT:
        speed_y = -speed_y

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)
    rect = pygame.Rect(rect_pos_x, rect_pos_y, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(screen, BLUE, rect)

    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
