import pygame
from pygame.locals import *
from Environment import Env
from Zombie import Zombie

_res = 200 # 4:3 times this _res
_size = _width,_height = (_res) * 4,(_res) * 3
_display = pygame.display.set_mode(_size)

_running = True
_FPS = 30
_Clock = pygame.time.Clock()

#test0 = Plant(40,40)
testenv = Env("heeheehoohoohahahihihuhuhehehyhyhwhwhoho")

while _running:
    # Getting the events
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            # scale mouse pos for resolution
            m_pos = [event.pos[0]*200//_res,event.pos[1]*200//_res]
            testenv.click(m_pos, event.button)
        elif event.type == QUIT:
            _running = False
            break

    # Some logic
    testenv.update_lawn()
    testenv.update_gyard()
    testenv.update_projs()

    # Some drawing
    _screen = pygame.Surface((800,600))
    
    #test0.draw(_screen)
    testenv.draw_lawn(_screen)
    testenv.draw_zombs(_screen)
    testenv.draw_projs(_screen)

    _screen = pygame.transform.scale(_screen,(_width,_height))
    _display.blit(_screen,Rect(0,0,_width,_height)) 
    
    pygame.display.update()

    # Miscellaneous
    _Clock.tick(_FPS)

print('Game iverbvbbasgdsafDSA gabagool!!!!!')
pygame.quit()
