import pygame

# Initialise pygame and create game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Set up Title for the window
pygame.display.set_caption("Balloon Pop!")

# Set Player image -- a SPACESHIP!
playerImg = pygame.image.load('spaceship.png')
x_value = 700
y_value = 268
y_change = 0

# Set balloon images -- added a spider so it looks scary!
balloonImg = pygame.image.load('spider.png')
b_x = 50
b_y = 268
b_y_change = 0


# use blit method to draw the spaceship & balloon on window
def player(x, y):
    window.blit(playerImg, (x, y))

def balloon(x, y):
    window.blit(balloonImg, (x, y))


# Set conditions for the game window to close
running = True
while running:

    # Set background window to black
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add key events for the Spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    y_value += y_change
    # Set boundaries for the window (5px margin)
    if y_value <= 5:
        y_value = 5
    elif y_value >= 531:
        y_value = 531

    # Draw the player and balloons after the screen background was set up
    balloon(b_x, b_y)
    player(x_value, y_value)
    pygame.display.update()