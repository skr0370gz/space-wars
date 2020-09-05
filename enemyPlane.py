import pygame
from random import *

class LowClassEnemy(pygame.sprite.Sprite):
    def __init__(self, backgroundSize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.destroyImages = []
        self.destroyImages.extend([pygame.image.load("images/enemy1_down1.png").convert_alpha(),pygame.image.load("images/enemy1_down2.png").convert_alpha(),pygame.image.load("images/enemy1_down3.png").convert_alpha(),pygame.image.load("images/enemy1_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = backgroundSize[0], backgroundSize[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-5*self.height,0)
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.resetPlane()

    def resetPlane(self):
        self.active = True
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-5*self.height,0)

class MiddleClassEnemy(pygame.sprite.Sprite):
    health = 8
    def __init__(self, backgroundSize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.imageHit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        self.destroyImages = []
        self.destroyImages.extend([pygame.image.load("images/enemy2_down1.png").convert_alpha(),pygame.image.load("images/enemy2_down2.png").convert_alpha(),pygame.image.load("images/enemy2_down3.png").convert_alpha(),pygame.image.load("images/enemy2_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = backgroundSize[0], backgroundSize[1]
        # slower compared to low class
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-10*self.height,-self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.health = MiddleClassEnemy.health
        self.hit = False
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.resetPlane()

    def resetPlane(self):
        self.active = True
        self.health = MiddleClassEnemy.health
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-10*self.height,-self.height)

class HighClassEnemy(pygame.sprite.Sprite):
    health = 20
    def __init__(self, backgroundSize):
        pygame.sprite.Sprite.__init__(self)
        self.imageHit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.destroyImages = []
        self.destroyImages.extend([pygame.image.load("images/enemy3_down1.png").convert_alpha(),pygame.image.load("images/enemy3_down2.png").convert_alpha(),pygame.image.load("images/enemy3_down3.png").convert_alpha(),pygame.image.load("images/enemy3_down4.png").convert_alpha(),pygame.image.load("images/enemy3_down5.png").convert_alpha(),pygame.image.load("images/enemy3_down6.png").convert_alpha() ])
        self.rect = self.image1.get_rect()
        self.width, self.height = backgroundSize[0], backgroundSize[1]
        # slower compared to low class
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-15*self.height,-5*self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.health = HighClassEnemy.health
        self.hit = False
    
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.resetPlane()

    def resetPlane(self):
        self.active = True
        self.health = HighClassEnemy.health
        self.rect.left, self.rect.top = randint(0,self.width-self.rect.width), randint(-15*self.height,-5*self.height)