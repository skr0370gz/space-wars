import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__ (self,backgroundSize):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/me3.png").convert_alpha()
        self.image2 = pygame.image.load("images/me4.png").convert_alpha()
        self.destroyImages = []
        self.destroyImages.extend([pygame.image.load("images/me_destroy_1.png").convert_alpha(),pygame.image.load("images/me_destroy_2.png").convert_alpha(),pygame.image.load("images/me_destroy_3.png").convert_alpha(),pygame.image.load("images/me_destroy_4.png").convert_alpha() ])
        self.rect = self.image1.get_rect()
        self.width, self.height = backgroundSize[0],backgroundSize[1]
        self.rect.left, self.rect.top = (self.width-self.rect.width)//2, (self.height-self.rect.height - 60)
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)
    
    def up(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed 
        else:
            self.rect.top = 0

    def down(self):
        if self.rect.bottom < self.height-60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60
    
    def left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else: 
            self.rect.left = 0
    
    def right(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width
    
    def reset(self):
        self.rect.left, self.rect.top = (self.width-self.rect.width)//2, (self.height-self.rect.height - 60)
        self.active = True 
        self.invincible = True
