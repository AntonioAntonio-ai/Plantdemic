# Lawn.py holds the Lawn class, which holds the currently planted plants,
# handles planting and digging up plants, and manages updating and drawing the
# plants, as well as deciding what lawnspace is taken or available.
import pygame
from pygame.locals import *
from pvzmath import *
from Plant import Plant
from Projectile import ProjMan

class Lawn():
    def __init__(self,in_id,parent):
        self.id = 0
        self.parent = parent
        self.image = None
        get_image_id(self)

        self.lawnspace = [] # Populated in allocate_lawn_id()
        self.slopeage = []  # [[x1,x2],[y1,y2],end height]
        allocate_lawn_id(self) # Fills lawnspace and linears
        
        self.plantlist = pygame.sprite.Group()
        self.projman = ProjMan()

##########Draw Functions#############################
    def draw_lawnspace(self,display):
        for col in self.lawnspace:
            for instance in col:
                #print(instance)
                pygame.draw.rect(display,(50,50,150),instance,width=1)
            
    def draw_lawn(self,display):
        display.blit(self.image,Rect(0,0,800,600))

    def draw_plants(self,display):
        for plant in self.plantlist.sprites():
            plant.draw(display)

    def draw_projs(self,display):
        if self.projman.has():
            self.projman.draw_all(display)

###############Plant Functions####################
    def add_plant(self,in_row,coords,in_id):
        #print(self,in_row,coords,in_id,self)
        plant = Plant(in_row,coords,in_id,self)
        self.plantlist.add(plant)
        #self.plants[pos[y]][pos[x]] = Plant(pos,in_id)

    def update_plants(self):
        for plant in self.plantlist.sprites():
            plant.update()

    def update_projs(self):
        if self.projman.has():
            self.projman.update(self.slopeage)

    # check for each
    def click(self,pos):
        for col in self.lawnspace:
            row = 0
            for space in col:
                row += 1
                if space.collidepoint(pos):
                    #print(row,[space.x,space.y],0)
                    self.add_plant(row,[space.centerx,space.centery],0)

    def create_proj(self,pos,z,in_id):
        self.projman.add(pos,z,in_id)

###############################################################################

def get_image_id(lawn):
    exec("get_image_{}(lawn)".format(lawn.id))

def get_image_0(lawn):
    lawn.image = pygame.image.load("img//lawn0.bmp")

###############################################################################
###############################################################################       
###############################################################################

def allocate_lawn_id(lawn):
    # should always allocate lawnspace from top to bottom, left to right
    exec("allocate_lawn_{}(lawn)".format(lawn.id))

def allocate_lawn_0(lawn):
    # add 20 lawnspaces in the back
    for ix in range(0,4):
        col = []
        for iy in range(0,5):
            col.append(Rect(13 + ix*99,116 + iy*96,93,91))
        lawn.lawnspace.append(col)
    # now add the 20 skewed lawnspaces in the front
    y_offset = 10
    for ix in range(0,4):
        col = []
        for iy in range(0,5):
            col.append(Rect(405 + ix*99,111 + iy*97 - y_offset,93,91))
        lawn.lawnspace.append(col)
        y_offset += 28
    ################################################
    #### self.path
    lawn.slopeage = [[405,800],[0,600],88] 
'''
    for iy in range(0,5):
        iy = 160 + iy*97
        row = [[0,iy,0],[405,iy,0],[1200,iy-230,230]]
        lawn.paths.append(row)
'''
#Lawn(3,4)
