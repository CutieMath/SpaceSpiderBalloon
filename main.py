import pygame

# Initialise pygame and create game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Set up Title for the window
pygame.display.set_caption("Balloon Pop!")

# Set Player image -- a SPACESHIP!
playerImg = pygame.image.load('spaceship.png')
x_value = 700
y_value = 270

# use blit method to draw the spaceship on window
def player(x, y):
    window.blit(playerImg, (x, y))


# Set conditions for the game window to close
running = True
while running:

    # Set background window to black
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add key event for the Spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up pressed!")
            if event.key == pygame.K_DOWN:
                print("Down pressed!")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("Key is released x")

    # Draw the player after the screen background was set up
    player(x_value, y_value)
    pygame.display.update()