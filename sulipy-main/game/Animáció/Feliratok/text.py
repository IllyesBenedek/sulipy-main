import pygame

WIDTH, HEIGHT = 600, 300
BG_COLOR = (140, 137, 246)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    pygame.display.update()

pygame.quit()
