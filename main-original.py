

from pygame_functions import *

import pickle

import pygame

import random

import os

import json

os.system("clear")

pygame.init()

 

win = pygame.display.set_mode((1915,1020))

pygame.display.set_caption("Nightmares Cult")

 

walk_Right = [pygame.image.load('images/r1.png'),pygame.image.load('images/r2.png'),pygame.image.load('images/r3.png'),pygame.image.load('images/r4.png'),pygame.image.load('images/r5.png'),pygame.image.load('images/r6.png'),pygame.image.load('images/r7.png'),pygame.image.load('images/r8.png')]

walk_Left = [pygame.image.load('images/l1.png'),pygame.image.load('images/l2.png'),pygame.imageload('images/l3.png'),pygame.image.load('images/l4.png'),pygame.image.load('images/l5.png'),pygame.image.load('images/l6.png'),pygame.image.load('images/l7.png'),pygame.image.load('images/l8.png')]

walk_Up = [pygame.image.load('images/u1.png'),pygame.image.load('images/u2.png'),pygame.image.load('images/u3.png'),pygame.image.load('images/u4.png'),pygame.image.load('images/u5.png'),pygame.image.load('images/u6.png'),pygame.image.load('images/u7.png'),pygame.image.load('images/u8.png')]

walk_Down = [pygame.image.load('images/d1.png'),pygame.image.load('images/d2.png'),pygame.image.load('images/d3.png'),pygame.image.load('images/d4.png'),pygame.image.load('images/d5.png'),pygame.image.load('images/d6.png'),pygame.image.load('images/d7.png'),pygame.image.load('images/d8.png')]

bg = pygame.image.load('images/bg.png')

d = pygame.image.load('idea/d.png')

 

with open("data_pick.pkl", "rb") as pickle_file:

    new_data = pickle.load(pickle_file)

       

x = new_data['x']

y = new_data['y']

width = 1915

height = 1020

vel = 6

 

clock = pygame.time.Clock()

 

right = False

left = False

up = False

down = False

walkCount = 0

 

white = (255,255,255)

red   = (255,  0,  0)

green = (  0,255,  0)

blue  = (  0,  0,255)

black  = (  0,  0,  0)

 

class player(pygame.sprite.Sprite):

   

    def __init__(self,x,y,width,height):

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.vel = vel

        self.left = False

        self.right = False

        self.up = False

        self.down = False

        self.walkCount = 0

        self.rect = (self.x + 1, self.y + 5, 64, 88)

 

    def draw(self, win):

        global walkCount

       

        if self.walkCount + 1 >= 32:

            self.walkCount = 0

 

        if self.right:

            win.blit(walk_Right[self.walkCount//4], (self.x,self.y))

            self.walkCount += 1

 

        elif self.left:

            win.blit(walk_Left[self.walkCount//4], (self.x,self.y))

            self.walkCount += 1

   

        if self.up:

            win.blit(walk_Up[self.walkCount//4], (self.x,self.y))

            self.walkCount += 1

 

        elif selfdown:

            win.blit(walk_Down[self.walkCount//4], (self.x,self.y))

            self.walkCount += 1

 

        self.rect = (self.x + 1, self.y + 5, 64, 88)

        pygame.draw.rect (win, red, selfrect,2)

 

class chest(pygame.sprite.Sprite):

 

    def __init__(self,x,y,width,height):

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.end = end

        self.path = [self.x, self.end]

        self.walkCount = 0

        self.vel = 3

        self.rect = (self.x + 17, self.y + 2, 31, 57)

       

    def draw(self,win):

        win.blit(d, (self.x, self.y))

        selfrect = (self.x + 17, self.y + 2, 31, 57)

        pygame.draw.rect(win, (255,0,0), self.rect,2)

 

class background(pygame.sprite.Sprite):

 

    def __init__(self,x,y,width,height):

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.end = end

        self.path = [selfx, self.end]

        self.walkCount = 0

        self.vel = 3

        self.rect = (self.x, self.y, 1915, 1020)

       

    def draw(self,win):

        win.blit(bg, (0,0))

        self.rect = (self.x, self.y, 1915, 1020)

        pygame.draw.rect(win, (255,0,0), self.rect,2)

 

player = player(x, y, 64, 64)

chest = chest (300, 410, 64, 64)

background = background (0, 0, 1915, 1020)

 

def game_state():

 

    running = True

    while running:

 

        clock.tick(100)

               

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

 

        keys = pygame.keyget_pressed()

 

        if keys[pygame.K_p]:

            data_dict = {

                "x": player.x,

                "y": player.y

            }

 

            with open("data_pick.pkl", "wb") as pickle_file:

                pickle.dump(data_dict, pickle_file)

 

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:

            player.x += player.vel

            player.left = False

            player.right = True

            player.up = False

            player.down = False

               

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:

            player.x -= player.vel

            player.left = True

            player.right = False

            player.up = False

            player.down = False

 

        if keys[pygame.K_w] or keys[pygame.K_UP]:

            player.y -= player.vel

            player.left = False

            player.right = False

            player.up = True

            player.down = False

           

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:

            player.y += player.vel

            player.left = False

            player.right = False

            player.up = False

            player.down = True

                       

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:

            player.x += playervel

            player.left = False

            player.right = True

            player.up = False

            player.down = False

               

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:

            player.x -= player.vel

            player.left = True

            player.right = False

            player.up = False

            player.down = False

 

        elif keys[pygame.K_w] or keys[pygame.K_UP]:

            player.y -= player.vel

            player.left = False

            player.right = False

            player.up = True

            player.down = False

           

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:

            player.y += player.vel

            player.left = False

            player.right = False

            player.up = False

            player.down = True

        else:

            player.left = False

            playerright = False

            player.up = False

            player.down = True

            player.walkCount = 0

 

        background.draw(win)

 

        player.draw(win)

 

        chest.draw(win)

 

        pygame.display.update()

 

game_state()

       

pygame.quit()

 

 

Inviato da Posta per Windows 10

 

	Mail priva di virus. www.avast.com

