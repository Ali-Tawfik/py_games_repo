from random import*
from pygame import*
from math import*
zompics=[]
screen=display.set_mode((1000,650))
screen.fill((0,255,0))
          
display.set_caption("*********************************ZOMBIES********************************")
myClock = time.Clock()

running=1
#_______________________________________________________________
while running==1:
    
        myClock.tick(60)
        display.update()
quit()
