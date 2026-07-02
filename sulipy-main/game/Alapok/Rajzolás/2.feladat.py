import pygame


# --- Színek ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Vonalak")

background_color = WHITE


# --- Fő ciklus ---
running = True
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # --- Kirajzolás ---
    screen.fill(background_color)

    pygame.draw.line(screen, BLACK, (50, 50), (550, 50), 1)
    pygame.draw.line(screen, BLACK, (50, 100), (550, 100), 3)
    pygame.draw.line(screen, BLACK, (50, 150), (550, 150), 6)
    pygame.draw.line(screen, BLACK, (50, 200), (550, 200), 10)
    pygame.draw.line(screen, BLACK, (50, 250), (550, 250), 15)

    pygame.display.update()


# --- Kilépés ---
pygame.quit()
