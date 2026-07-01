import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300), pygame.RESIZABLE)
pygame.display.set_caption("Alapok")

running = True
while running:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            print(f"Egér pozició: {event.pos}")

        elif event.type == pygame.VIDEORESIZE:
            print(f"Ablak új mérete: {event.w} x {event.h}")

    pygame.display.update()
pygame.quit()
