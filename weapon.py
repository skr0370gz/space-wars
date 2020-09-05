import pygame

class BasicBullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        #initialization
        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position 
        self.speed = 12
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <0:
            self.active = False
    
    def resetBullet(self,position):
        self.rect.left, self.rect.top = position 
        self.active = True

class AdvancedBullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        #initialization
        self.image = pygame.image.load("images/life.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position 
        self.speed = 30
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <0:
            self.active = False
    
    def resetBullet(self,position):
        self.rect.left, self.rect.top = position 
        self.active = True