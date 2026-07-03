import pygame


# --- Színek ---
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


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
            if event.key == pygame.K_r:
                background_color = RED
            elif event.key == pygame.K_g:
                background_color = GREEN

    # --- Kirajzolás ---
    screen.fill(background_color)
    pygame.display.update()


# --- Kilépés ---
pygame.quit()
