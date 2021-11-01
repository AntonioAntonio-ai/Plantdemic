import pygame
from pygame.locals import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self,row,in_id,gyard):
        super().__init__()

        self.id = in_id
        self.parent = gyard
        self.img = pygame.image.load('img//zombplace.bmp')
        self.img.set_colorkey((1,33,99))
        self.img = pygame.transform.scale(self.img, (64,97))

        self.timer = 0
        self.nxtdir = [16,16,1] # this must be like this
        self.next = 0

        self.row = row
        self.rect = self.img.get_rect()
        self.rect.x = 800
        self.rect.y = -18 + row * 96

    def draw(self,display):
        display.blit(self.img,self.rect)

    def update(self):
        if self.timer < 15:
            self.rect.x -= not (self.timer % self.nxtdir[0])
            self.rect.y += not (self.timer % self.nxtdir[1])
            self.nxtdir[2] -= 1
        elif self.timer == 30:
            self.timer = 0
        self.timer += 1

        if self.nxtdir[2] == 0:
            if self.next < len(self.parent.path):
                self.nxtdir = self.parent.path[self.next].copy()
            
            self.next += 1
