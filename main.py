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
# death: Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


import pygame
import random
import math
from pygame import mixer

# Initialise pygame and create game window
pygame.init()
window = pygame.display.set_mode((800, 600))

# Set up Title for the window
pygame.display.set_caption("Balloon Pop!")

# Set up background
background = pygame.image.load('image/background.png')

# Player image -- a SPACESHIP!
playerImg = pygame.image.load('image/spaceship.png')
playerX = 667
playerY = 268
playerYChange = 0

# balloon image -- added a spider so it looks scary!
balloonImg = pygame.image.load('image/spider.png')
balloonX = 10
balloonY = random.randint(0, 456)
balloonYChange = 2

# bullet image -- a fireball
# set bullet state for it's appearance
# "ready" : hidden
# "fire" : appear on screen
bulletImg = pygame.image.load('image/bullet.png')
bulletX = 667
bulletY = 0
bulletXChange = 5
bulletState = "ready"

# track missed bullets
missed_value = 0
font = pygame.font.Font('font/Bungee-Regular.ttf', 30)
textX = 250
textY = 10

# end game text
overText = pygame.font.Font('font/Bungee-Regular.ttf', 50)


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


# calculate if the bullet and balloon collides
# use Distance Formula (https://tinyurl.com/hgh57xt)
def isCollision(balloonX, balloonY, bulletX, bulletY):
    distance_D = math.sqrt(math.pow((balloonX - bulletX), 2) + math.pow((balloonY - bulletY), 2))
    if distance_D < 50:
        return True
    else:
        return False


# display missed shots on the screen
def show_missed(x, y):
    missed = font.render("Missed Shots: " + str(missed_value), True, (255, 230, 242))
    window.blit(missed, (x, y))


# function to end the game
def end():
    text = overText.render("YOU WON THE GAME!", True, (255, 230, 242))
    window.blit(text, (150, 250))
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()

        show_missed(textX, textY)
        balloon(balloonX, balloonY)
        player(playerX, playerY)
        pygame.display.update()


# Set conditions for the game window to close
running = True
while running:

    # Set background
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
                    shootSound = mixer.Sound("sound/shoot.wav")
                    shootSound.play()
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
        # track missed bullets
        missed_value += 1
    if bulletState == "fire":
        fire(bulletX, bulletY)
        bulletX -= bulletXChange

    # when the balloon is hit, end the game
    collision = isCollision(balloonX, balloonY, bulletX, bulletY)
    if collision:
        hitSound = mixer.Sound("sound/hit.wav")
        hitSound.play()
        balloonImg = pygame.image.load('image/skull.png')
        end()

    # Draw the player and balloons after the screen background was set up
    balloon(balloonX, balloonY)
    player(playerX, playerY)
    show_missed(textX, textY)
    pygame.display.update()
