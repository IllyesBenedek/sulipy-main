import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 600, 300
BLUE = (0, 0, 255)
BG_COLOR = (127, 127, 127)


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rect_pos_x = 10
rect_pos_y = 20

clock = pygame.time.Clock()


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    screen.fill(BG_COLOR)

    rect_pos_x += 5
    rect_pos_y += 2
    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)

    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
