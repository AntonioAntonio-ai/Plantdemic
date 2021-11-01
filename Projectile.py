# ProjMan a projectile manager.
import pygame
from pygame import *

class ProjMan():
    def __init__(self,parent=None):
        self.projs = pygame.sprite.Group()
        self.parent = parent

    def draw_all(self, display):
        for proj in self.projs.sprites():
            proj.draw_shadow(display)
            proj.draw(display)
    
    def update(self,slopeage):
        for proj in self.projs.sprites():
            proj.update_shadow(slopeage)
            proj.update()

    def add(self,coords,z,in_id):
        self.projs.add(Proj(coords,z,in_id))

    def has(self,target=False):
        if target:
            print("Projectile.py ProjMan.has(target) no implementation error")
        else:
            return(self.projs.sprites() != [])

class Proj(pygame.sprite.Sprite):
    def __init__(self,coords,z,in_id):
        super().__init__()

        self.id = in_id
        
        self.img = None
        get_img_id(self)
        self.img.set_colorkey((1,33,99))
        self.img = pygame.transform.scale(self.img, (16,16))

        self.original_z = z + 44
        self.z = z + 44
        self.rect = self.img.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]

    def draw_shadow(self,display):
        pygame.draw.circle(display,(0,0,0),[self.rect.centerx,self.rect.centery+self.z],8)
    
    def draw(self,display):
        #self.rect.y -= self.z
        display.blit(self.img,self.rect)
        #self.rect.y += self.z

    def update_shadow(self, m):
        # m is the self.slopeage from a Lawn object
        if self.rect.x >= m[0][0] and self.rect.x < m[0][1]:
            if self.rect.y >= m[1][0] and self.rect.y < m[1][1]:
                self.z = self.original_z - (self.rect.x - m[0][0]) / (m[0][1] - m[0][0]) * m[2] // 1
    
    def update(self):
        update_id(self)
        if self.rect.x > 800 or self.z == 0:
            self.kill()

##############################################################

def get_img_id(proj):
    exec("get_img_{}(proj)".format(proj.id,proj))

def get_img_0(proj):
    proj.img = pygame.image.load("img//proj.bmp")

#######

def update_id(proj):
    exec("update_{}(proj)".format(proj.id))

def update_0(proj):
    proj.rect.x += 4
