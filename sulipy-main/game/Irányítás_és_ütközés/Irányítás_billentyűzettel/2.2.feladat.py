import pygame
import random


# --- Beállítások ---
WIDTH = 1280
HEIGHT = 620
SPEED = 5

# --- Inicializálás ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

animal_images = [
    "Irányítás_és_ütközés/Irányítás_billentyűzettel/img/goat.png",
    "Irányítás_és_ütközés/Irányítás_billentyűzettel/img/gorilla.png",
    "Irányítás_és_ütközés/Irányítás_billentyűzettel/img/monkey.png",
    "Irányítás_és_ütközés/Irányítás_billentyűzettel/img/penguin.png",
    "Irányítás_és_ütközés/Irányítás_billentyűzettel/img/whale.png",
]

animal = pygame.image.load(random.choice(animal_images)).convert_alpha()
animal_x = WIDTH / 2
animal_y = HEIGHT / 2
animal_rect = animal.get_rect(center=(animal_x, animal_y))

running = True


# --- Fő ciklus ---
while running:

    # --- Események kezelése ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and animal_rect.right <= WIDTH:
        animal_x += SPEED
    elif keys[pygame.K_LEFT] and animal_rect.left >= 0:
        animal_x -= SPEED

    if keys[pygame.K_UP] and animal_rect.top >= 0:
        animal_y -= SPEED
    elif keys[pygame.K_DOWN] and animal_rect.bottom <= HEIGHT:
        animal_y += SPEED

    animal_rect = animal.get_rect(center=(animal_x, animal_y))

    # --- Kirajzolás ---
    screen.fill((140, 137, 246))
    screen.blit(animal, animal_rect)
    pygame.display.update()
    clock.tick(60)


# --- Kilépés ---
pygame.quit()
