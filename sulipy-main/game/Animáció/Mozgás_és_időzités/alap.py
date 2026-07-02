import pygame


# --- Beállítások ---
WIDTH, HEIGHT = 600, 300


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    pygame.display.update()


# --- Kilépés ---
pygame.quit()
