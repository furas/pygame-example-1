# - standard modules - order A-Z
import json
import os
import pickle
import random
# - external modules -
import pygame


# --- constatants --- (UPPER_CASE_NAMES)

WIDTH  = 1915
HEIGHT = 1020

WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
BLACK = (  0,  0,  0)

CONFIG_PATH = "data_pick.pkl"

HOME_PATH = os.path.abspath(os.path.dirname(__file__))  # it will needed to run from different folder
print('HOME_PATH:', HOME_PATH)

# --- classes --- (CamelCaseNames)


class Player(pygame.sprite.Sprite):  # PEP8: UpperCaseName for classes - `class Player`


    def __init__(self, x, y, width, height, vel=6):  # PEP8: spaces after `,`
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0  # PEP8: `lower_case_names` for variables

        # all images inside class
        self.walk = {
            'right': [pygame.image.load(os.path.join(HOME_PATH, f'images/r{number}.png')) for number in range(1, 5)],
            'left':  [pygame.image.load(os.path.join(HOME_PATH, f'images/l{number}.png')) for number in range(1, 5)],
            'up':    [pygame.image.load(os.path.join(HOME_PATH, f'images/u{number}.png')) for number in range(1, 5)],
            'down':  [pygame.image.load(os.path.join(HOME_PATH, f'images/d{number}.png')) for number in range(1, 5)],
        }            

        #self.walk = {
        #    'right': [
        #        pygame.image.load('images/r1.png'),
        #        pygame.image.load('images/r2.png'),
        #        pygame.image.load('images/r3.png'),
        #        pygame.image.load('images/r4.png'),
        #        pygame.image.load('images/r5.png'),
        #        pygame.image.load('images/r6.png'),
        #        pygame.image.load('images/r7.png'),
        #        pygame.image.load('images/r8.png')  
        #    ],
        #    'left': [
        #        pygame.image.load('images/l1.png'),
        #        pygame.image.load('images/l2.png'),
        #        pygame.image.load('images/l3.png'),
        #        pygame.image.load('images/l4.png'),
        #        pygame.image.load('images/l5.png'),
        #        pygame.image.load('images/l6.png'),
        #        pygame.image.load('images/l7.png'),
        #        pygame.image.load('images/l8.png')
        #    ],
        #    'up': [
        #        pygame.image.load('images/u1.png'),
        #        pygame.image.load('images/u2.png'),
        #        pygame.image.load('images/u3.png'),
        #        pygame.image.load('images/u4.png'),
        #        pygame.image.load('images/u5.png'),
        #        pygame.image.load('images/u6.png'),
        #        pygame.image.load('images/u7.png'),
        #        pygame.image.load('images/u8.png')
        #    ],
        #    'down': [
        #        pygame.image.load('images/d1.png'),
        #        pygame.image.load('images/d2.png'),
        #        pygame.image.load('images/d3.png'),
        #        pygame.image.load('images/d4.png'),
        #        pygame.image.load('images/d5.png'),
        #        pygame.image.load('images/d6.png'),
        #        pygame.image.load('images/d7.png'),
        #        pygame.image.load('images/d8.png'),
        #    ]
        #}     
        
        # to draw object
        self.rect = pygame.Rect(x, y, width, height)
        self.image = self.walk['right'][0]   # default image at start

        # to draw hitbox
        #self.hitbox_rect = pygame.Rect(x+1, y+5, 64, 88)
        self.hitbox_rect = pygame.Rect(x+1, y+5, width-(1*2), height-(5*2))
        self.hitbox_color = RED
           

    def move(self):       
        """only move, without draw"""
        
        if self.walk_count + 1 >= 4*4:
            self.walk_count = 0

        if self.right:
            if self.rect.right < win.get_rect().right:  #  don' leave map/screen
                # move object
                self.rect.x += self.vel
                # move hitbox
                self.hitbox_rect.x += self.vel

                # change animation's frame                
                frame = self.walk_count//4
                self.image = self.walk['right'][frame]
                self.walk_count += 1

        elif self.left:
            if self.rect.left > win.get_rect().left:  #  don' leave map/screen
                # move object
                self.rect.x -= self.vel
                # move hitbox
                self.hitbox_rect.x -= self.vel
                
                # change animation's frame                
                frame = self.walk_count//4
                self.image = self.walk['left'][frame]
                self.walk_count += 1

        # if you use `elif` then it will not move diagonal.
        if self.up:
            if self.rect.top > win.get_rect().top:  #  don' leave map/screen
                # move object
                self.rect.y -= self.vel
                # move hitbox
                self.hitbox_rect.y -= self.vel
                
                # change animation's frame                
                frame = self.walk_count//4
                self.image = self.walk['up'][frame]
                self.walk_count += 1

        elif self.down:
            if self.rect.bottom < win.get_rect().bottom:  #  don' leave map/screen
                # move object
                self.rect.y += self.vel
                # move hitbox
                self.hitbox_rect.y += self.vel
                
                # change animation's frame                
                frame = self.walk_count//4
                self.image = self.walk['down'][frame]
                self.walk_count += 1

    
    def draw(self, win, offset_x, offset_y):
        """only draw, without move"""
        
        # object + offset
        temp_rect = self.rect.move(offset_x, offset_y)
        win.blit(self.image, temp_rect)
        
        # hitbox + offset
        temp_rect = self.hitbox_rect.move(offset_x, offset_y)
        pygame.draw.rect(win, self.hitbox_color, temp_rect, 2)


    def handle_keys(self, keys):
        self.left  = False
        self.right = False
        self.up    = False
        self.down  = False
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.right = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.left  = True
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.up    = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.down  = True
            

class Chest(pygame.sprite.Sprite):  # PEP8: UpperCaseName for classes


    def __init__(self, x, y, width, height, end, vel=3):  # PEP8: spaces after `,`
        self.end = end
        self.path = [x, end]
        self.walk_count = 0
        self.vel = vel

        # to draw object
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.surface.Surface(self.rect.size)
        self.image.fill(BLUE)
        #self.image = pygame.image.load(os.path.join(HOME_PATH, 'images/chest.png'))

        # to draw hitbox
        self.hitbox_rect = pygame.Rect(x+17, y+2, 31, 57)
        self.hitbox_color = RED


    def draw(self, win ,offset_x, offset_y):
        # object + offset
        temp_rect = self.rect.move(offset_x, offset_y)
        win.blit(self.image, temp_rect)
        
        # hitbox + offset
        temp_rect = self.hitbox_rect.move(offset_x, offset_y)
        pygame.draw.rect(win, self.hitbox_color, temp_rect, 2)


    def move(self):
        pass

        
class Background(pygame.sprite.Sprite):  # PEP8: UpperCaseName for classes


    def __init__(self, x, y, width, height):  # PEP8: spaces after `,`
        self.walk_count = 0
        self.vel = 3

        # to draw object
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        #self.image = pygame.image.load(os.path.join(HOME_PATH, 'images/bg.png'))
        self.image = pygame.surface.Surface(self.rect.size)
        self.image.fill(GREEN)
        
        # to draw hitbox
        self.hitbox_rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.hitbox_color = RED


    def draw(self, win ,offset_x, offset_y):
        # object + offset
        temp_rect = self.rect.move(offset_x, offset_y)
        win.blit(self.image, temp_rect)
        
        # hitbox + offset
        temp_rect = self.hitbox_rect.move(offset_x, offset_y)
        pygame.draw.rect(win, self.hitbox_color, temp_rect, 2)


    def move(self):
        pass

 
# --- functions --- (lower_case_names)

def load_config():
    with open(CONFIG_PATH, "rb") as pickle_file:
        data = pickle.load(pickle_file)
    return data
    
def save_config(data):
    with open(CONFIG_PATH, "wb") as pickle_file:
        pickle.dump(data, pickle_file)

def game_state():
    
    clock = pygame.time.Clock()

    running = True

    offset_x = 0
    offset_y = 0
    
    while running:
        clock.tick(100)

        # - events -
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #    pygame.quit()  # if you use `quit` inside loop then better add `exit()` or use `return` to skip rest of code
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            config = {"x": player.x, "y": player.y}
            save_config(config)
            
        player.handle_keys(keys)
        
        # - moves (without draws) -
        
        player.move()
        
        offset_x = win.get_rect().centerx - player.rect.centerx
        offset_y = win.get_rect().centery - player.rect.centery
        
        for chest in all_chests:        
            chest.move()
        
        # - draws (without moves) -
        
        win.fill(BLACK)
        
        background.draw(win, offset_x, offset_y)
        player.draw(win, offset_x, offset_y)
        for chest in all_chests:        
            chest.draw(win, offset_x, offset_y)
        
        pygame.display.update()

# --- main ---

#os.system("clear")

# - init -

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nightmares Cult")

# - settings -

try:
    config = load_config()
    x = config['x']
    y = config['y']
except FileNotFoundError:
    x = 0
    y = 0    

# - objects -

# `UpperCaseNames` for classes - it is more readable `player = Player()`
background = Background(0, 0, WIDTH, HEIGHT)
player = Player(x, y, 64, 64, 6)

all_chests = [
    Chest(300, 410, 64, 64, 500, 3),
    Chest(700, 700, 64, 64, 500, 3),
]

# - mainloop - 

game_state()

# - end -       

pygame.quit()

