# Environment.py holds the Env and ProjMan classes. Env manages which level it
# is, which location and time of day it is, the falling sun, gravestones and
# other objects like that, alongside telling Lawn what layout the lawn should
# be and telling Grave what zombie waveset should occur and when.
# UPDATE: Env also handles the hud including seeds and the shovel
import pygame
from pygame.locals import *
from Lawn import Lawn
from Graveyard import Gyard

class Env():
    def __init__(self, in_id):
        self.lawn = Lawn(in_id,self)
        self.gyard = Gyard(in_id,self)
        self.debug = False

########## Draw Functions #################
    def draw_lawn(self, display):
        self.lawn.draw_lawn(display)
        self.lawn.draw_plants(display)
        
        if self.debug:
            self.lawn.draw_lawnspace(display)

    def draw_zombs(self, display):
        self.gyard.draw_zombies(display)

    def draw_projs(self,display):
        self.lawn.draw_projs(display)
        self.gyard.draw_projs(display)

########### Management Functions ##########
    def update_lawn(self):
        self.lawn.update_plants()

    def update_gyard(self):
        self.gyard.update_zombies()

    def update_projs(self):
        self.lawn.update_projs()
        self.gyard.update_projs()

    def click(self, pos, button):
        if button < 2:
            self.lawn.click(pos)
        else:
            self.gyard.click(pos)

########## Specific Objects ################
    def get_shadow(self, obj):
        pass
