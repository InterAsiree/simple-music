import sys
import pygame
from pygame import  *
from uimaker import *

tui=aui(900,600)
#pictures
tui.pics('red.png')
tui.pics('green.png')
#ui
tui.cbutn(100,100,200,200,0,1)
tui.ct_pic(1820,100,1)
tui.cljk(400,400,200,200,0,1,1)
#gb
gbsd_1=0
#main
while True:
    #event
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type==pygame.MOUSEBUTTONDOWN:
            if ev.button==1:
                msh=ev.pos
                tui.sure(msh[0],msh[1])
            if uitalk[0]>=1:
                pygame.quit()
                sys.exit()
    #draw
    tui.uidraw()
    pygame.display.flip()