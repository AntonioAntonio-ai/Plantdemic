import pygame
from pygame.locals import *

class Plant(pygame.sprite.Sprite):
    def __init__(self, row, coords, in_id, lawn):
        super().__init__()

        self.id = in_id
        self.img = pygame.image.load('img//plantplace.bmp')
        self.img.set_colorkey((1,33,99))
        self.img = pygame.transform.scale(self.img, (64,64))

        self.timer = 0 # used for the animation, which controls shooting, etc.
        self.lawn = lawn

        self.row = row
        self.rect = self.img.get_rect()
        # coords consists of [x,y]
        #print(coords)
        self.rect.centerx = coords[0]
        self.rect.centery = coords[1]

        # change the plant's elevation
        self.z = 0
        
        m = self.lawn.slopeage
        if self.rect.x >= m[0][0] and self.rect.x < m[0][1]:
            if self.rect.y >= m[1][0] and self.rect.y < m[1][1]:
                self.z = (self.rect.x - m[0][0]) / (m[0][1] - m[0][0]) * m[2] // 1

    def draw(self, display):
        display.blit(self.img,self.rect)

    def update(self):
        if self.timer == 60:
            self.timer = 0
            self.create_proj()
        self.timer += 1

    def create_proj(self):
        self.lawn.create_proj([self.rect.x,self.rect.y],self.z,self.id)
