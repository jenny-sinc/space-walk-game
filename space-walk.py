import pygame, sys
from pygame.locals import *
import random

# initializes all PyGame modules. 
pygame.init()

# info to create the main display
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 400
CAPTION = "Space walk"
ICON = pygame.image.load("./doug-sprite/doug_0.png")

# set frame rate
clock = pygame.time.Clock()
FPS = (60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)


# define player action variables
moving_left = False
moving_right = False

# define colours
GRASS = (65,152,10)

def draw_bg():
    screen.fill(GRASS)

class Dog(pygame.sprite.Sprite):
    def __init__(self, character_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.character_type = character_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'./img/{self.character_type}/Idle/0.png')
        
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def move(self, moving_left, moving_right):
        # reset movement variables
        dx, dy = 0, 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    

# PLAYER (DOUG)
doug = Dog('doug', int(0.2*SCREEN_WIDTH), (SCREEN_HEIGHT/2), 2, 5)

run = True
while run:
    clock.tick(FPS)

    draw_bg()
    doug.draw()
    doug.move(moving_left, moving_right)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        # key pressed
        if event.type == pygame.KEYDOWN:
            # quick quit via ESC key
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True

        # key un-pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.display.update()

pygame.quit()