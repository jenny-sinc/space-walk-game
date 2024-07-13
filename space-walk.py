import pygame, sys
from pygame.locals import *
import random

# initializes all PyGame modules. 
pygame.init()

# info to create the main display
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 400
CAPTION = "Space walk"
ICON = pygame.image.load("./doug-sprite/doug_0.png")
FPS = pygame.time.Clock()
FPS.tick(60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)

class Dog(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('./doug-sprite/doug_2.png')
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def draw(self):
        screen.blit(self.image, self.rect)

# PLAYER (DOUG)
doug = Dog(int(0.2*SCREEN_WIDTH), (SCREEN_HEIGHT/2), 2)

run = True
while run:

    doug.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()