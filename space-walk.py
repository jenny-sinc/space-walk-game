import pygame, sys
from pygame.locals import *
import os, random

# initializes all PyGame modules. 
pygame.init()

# info to create the main display
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 400
CAPTION = "Space walk"
ICON = pygame.image.load("./img/Space/space_doug.png")

# set frame rate
clock = pygame.time.Clock()
FPS = (60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)

# define game variables

# define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# define colours
GRASS = (65,152,10)
BOUNDARY = (19,109,21)

# define boundaries of game=space
x_lower, x_upper = 0, SCREEN_WIDTH
y_lower, y_upper = 0, SCREEN_HEIGHT

def draw_bg():
    screen.fill(GRASS)
    pygame.draw.line(screen, BOUNDARY, (0, 0), (SCREEN_WIDTH, 0), 5)
    pygame.draw.line(screen, BOUNDARY, (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BOUNDARY, (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BOUNDARY, (0, SCREEN_HEIGHT), (0, 0), 5)

class Dog(pygame.sprite.Sprite):
    def __init__(self, character_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.character_type = character_type
        self.speed = speed
        self.direction = 1 if (character_type == "doug") else -1
        self.flip = False if (character_type == "doug") else True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()


        # load all images for characters
        animation_types = ['Idle', 'Walk']
        for animation in animation_types:
            # reset animation types list
            temp_list = []
            # counting number of images (frames) for each animation
            num_frames = len(os.listdir(f'./img/{animation}/{self.character_type}'))
            # iterate through each frame & appending to temp_list 
            for i in range(num_frames):
                img_folder = f'./img/{animation}/{self.character_type}'
                img = pygame.image.load(f'{img_folder}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                temp_list.append(img)
            # append temp_list (one complete animation) into overall animation list
            self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def move(self, moving_left, moving_right, moving_up, moving_down):
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
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # check collision with boundaries of screen
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
        if self.rect.top + dy <= 0:
            self.rect.top = 0
            dy = 0
        if self.rect.right + dx > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            dx = 0
        if self.rect.left + dy < 0:
            self.rect.left = 0
            dx = 0


    def update_animation(self):
        # update animation using a timer
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update (using get_ticks & cooldown)
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if animation has finished, reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        #check if new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    

# PLAYER (DOUG)
doug = Dog('doug', int(0.2*SCREEN_WIDTH), (SCREEN_HEIGHT/2), 2, 3)
dog1 = Dog('dog1', int(0.5*SCREEN_WIDTH), (SCREEN_HEIGHT/2), 2, 3)

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    doug.update_animation()
    dog1.update_animation()
    doug.draw()
    dog1.draw()

    #update player actions (only so long as the player is alive)
    if doug.alive:
        if (moving_left or moving_right or moving_up or moving_down):
            doug.update_action(1) # action 1: walk
        else:
            doug.update_action(0) # action 0: idle


    doug.move(moving_left, moving_right, moving_up, moving_down)
    
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        # key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # quick quit via ESC key
                run = False
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True

        # key un-pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False

    pygame.display.update()

pygame.quit()