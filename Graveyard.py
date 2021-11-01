# Graveyard.py holds the Gyard class, which manages zombies and zombie waves
# and all sorts of zombie drawing and updating and movement and junk.
import pygame
from pygame.locals import *
from Zombie import Zombie
from Projectile import ProjMan

class Gyard():
    def __init__(self,in_id,parent):
        self.id = in_id
        self.parent = parent

        self.zombies = pygame.sprite.Group()
        # self.path is [[x1,y1,t1], [x2,y2,t2]...];
        # x = delay between x steps, y = same as x but with y, t = time left
        # (16 means no steps)
        self.path = [[1,3,400],[1,16,400]]
        self.projman = ProjMan()

######### Draw functions  ############################
    def draw_zombies(self,display):
        for zombie in self.zombies.sprites():
            zombie.draw(display)

    def draw_projs(self,display):
        if self.projman.has():
            self.projman.draw_all(display)

###### Zombie functions ###########################
    def update_zombies(self):
        for zombie in self.zombies.sprites():
            zombie.update()

    def update_projs(self):
        if self.projman.has():
            self.projman.update()

    def click(self, pos):
        row = (pos[1] // 97) % 5
        self.zombies.add(Zombie(row,self.id,self))
