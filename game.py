# importing all the libraries needed to create the game.
import pygame
import os
import random
import time

# init the font that will be used within the game window.
pygame.font.init()

# Creating the game window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Nebula of Orion")


# loading all assets of the game
RED_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))

# Loading the main player ship
YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_yellow.png"))


# Loading lasers
RED_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# DesignIsOrion DesignIsOrion DesignIsOrion DesignIsOrion DesignIsOrion DesignIsOrion

# Loading the background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Loading Ships


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


# the game main loop that checks collisions, etc

def main():
    run = True
    FPS = 60  # frames per second. higher the number the faster the game moves
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 30)

    ship = Ship(300, 550)

    clock = pygame.time.Clock()

    def redraw_window():
        # blit is a method that takes one of the images and draws it at the postion we will place it.
        WIN.blit(BG, (0, 0))
        # draw text of lives and level
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 225, 225))
        level_label = main_font.render(f"Level: {level}", 1, (255, 225, 225))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # draw ship

        ship.draw(WIN)

        pygame.display.update()  # continues to refresh to update game status

    while run:
        clock.tick(FPS)
        redraw_window()
        # checking the game events

        # Checking to see if the game is quit user clicking the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main()
