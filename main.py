#
# Made by Yuxin 5th September, 2020
# yuxin_ye@protonmail.com
#
# image Used:
# Background: 800 x 600 <a href='https://www.freepik.com/vectors/star'>Star vector created by vectorpouch - www.freepik.com</a>
# Spaceship: 128px <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Spider Balloon: 128px <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# background:
# bullet: 64px


import pygame
import random

# Initialise pygame and create game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Set up Title for the window
pygame.display.set_caption("Balloon Pop!")

# Set up background
background = pygame.image.load('background.png')

# Player image -- a SPACESHIP!
playerImg = pygame.image.load('spaceship.png')
playerX = 667
playerY = 268
playerYChange = 0

# balloon image -- added a spider so it looks scary!
balloonImg = pygame.image.load('spider.png')
balloonX = 10
balloonY = random.randint(0, 456)
balloonYChange = 2

# bullet image -- a fireball
# set bullet state for it's appearance
# "ready" : hidden
# "fire" : appear on screen
bulletImg = pygame.image.load('bullet.png')
bulletX = 667
bulletY = 0
bulletXChange = 5
bulletState = "ready"


# use blit method to draw the spaceship & balloon on window
def player(x, y):
    window.blit(playerImg, (x, y))

def balloon(x, y):
    window.blit(balloonImg, (x, y))

# show bullet when spaceBar is pressed
# use y + 30 to make sure the bullet is shooting from the middle
def fire(x, y):
    global bulletState
    bulletState = "fire"
    window.blit(bulletImg, (x, y + 30))


# Set conditions for the game window to close
running = True
while running:

    # Set background to black
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerYChange -= 10
            if event.key == pygame.K_DOWN:
                playerYChange += 10
            if event.key == pygame.K_SPACE:
                # make sure the bullet is only appearing when it's state is "ready"
                # witch means when the bullet shoot outside window
                if bulletState == "ready":
                    bulletY = playerY
                    fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYChange = 0

    # Player move
    playerY += playerYChange
    # Balloon move
    balloonY += balloonYChange

    # Set window boundaries for player
    if playerY <= 5:
        playerY = 5
    elif playerY >= 467:
        playerY = 467

    # Set window boundaries and movements for balloon
    if balloonY <= 5:
        balloonY = 5
        balloonYChange = 2
    elif balloonY >= 467:
        balloonY = 467
        balloonYChange = -2

    # Set window boundaries and movements for bullet
    if bulletX <= 0:
        bulletX = 667
        # when the bullet shoot outside window, change the state to ready
        bulletState = "ready"
    if bulletState == "fire":
        fire(bulletX, bulletY)
        bulletX -= bulletXChange


    # Draw the player and balloons after the screen background was set up
    balloon(balloonX, balloonY)
    player(playerX, playerY)
    pygame.display.update()