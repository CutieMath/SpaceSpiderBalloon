import pygame

# Initialise pygame and create game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Set conditions for the game window to close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False