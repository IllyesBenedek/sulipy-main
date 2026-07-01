import pygame


# --- Színek ---
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# --- Billentyű - szín szótár ---
COLOR_MAP = {
    pygame.K_r: RED,
    pygame.K_g: GREEN,
    pygame.K_b: BLUE,
    pygame.K_y: YELLOW,
}


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Színek")

background_color = WHITE


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in COLOR_MAP:
                background_color = COLOR_MAP[event.key]

    # --- Ablakcím frissítése ---
    pygame.display.set_caption(f"Háttérszín RGB: {background_color}")

    # --- Kirajzolás ---
    screen.fill(background_color)
    pygame.display.update()


# --- Kilépés ---
pygame.quit()
