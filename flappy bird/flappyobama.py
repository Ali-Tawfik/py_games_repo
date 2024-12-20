from pygame import*
from random import*
import glob
diary=open("diary.txt","r")
topscore=int(diary.readline())
totalflaps=int(diary.readline())
diary.close()
screen=display.set_mode((1000,700))
running=True
init()
startscreen= image.load("backgrounds/startscreen.jpg")
pausescreen= image.load("backgrounds/pausescreen.jpg")
gameover= image.load("backgrounds/gameover.jpg")
diarypic= image.load("backgrounds/diary.jpg")
back=image.load("backgrounds/back.jpg")
instructions=image.load("backgrounds/instructions.jpg")
animation=[image.load("flappy1.png"),image.load("flappy2.png"),image.load("flappy3.png"),image.load("flappy4.png")]
animationnum=0
backpos=0
clock = time.Clock()
mainmenu=True
diaryfont = font.SysFont('Tw Cen MT Condensed Extra Bold',120)
        #Rect`          vy   onGround   Upkey
bird=[Rect(75,400,46,32),0,False,False,0]
rect=0
vy=1
Onground=2
Upkey=3
Score=4
mainmenurects=[Rect(108,368,195,68),Rect(90,450,225,70),Rect(110,530,195,70),Rect(122,619,178,65)]
m1=False
poles=[]
mixer.music.load("music.mp3")
mixer.music.play()
while mainmenu:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button==1:
                m1=True
    mx,my=mouse.get_pos()
    screen.blit(startscreen,(0,0))
    for i in  range (len(mainmenurects)):
        if mainmenurects[i].collidepoint((mx,my)):
            draw.rect(screen,(0,255,0),mainmenurects[i],5)
            if m1==True:
                if i==0:
                    mainmenu=False
                elif i ==1:
                    diary=True
                    screen.blit(diarypic,(0,0))
                    screen.blit(diaryfont.render(str(topscore) ,True,(226,194,156)),(190,280))
                    screen.blit(diaryfont.render(str(totalflaps) ,True,(226,194,156)),(590,305))
                    while diary:
                        for e in event.get():
                            if e.type == KEYDOWN:
                                if e.key == K_ESCAPE:
                                    diary=False
                        display.flip()
                elif i==2:
                    quit()
                elif i==3:
                    about=True
                    while about:
                        screen.blit(instructions,(0,0))
                        for e in event.get():
                            if e.type == KEYDOWN:
                                if e.key == K_ESCAPE:
                                    about=False
                        display.flip()
    m1=False
    display.flip()
        
polesdelay=0
polespawner=0
spawnpoles=False
ScoreFont = font.SysFont('Tw Cen MT Condensed Extra Bold',40)
ScoreFont2 = font.SysFont('Tw Cen MT Condensed Extra Bold',90)
def update(back,backpos,bird,animation,animationnum,poles,topscore,totalflaps):
    screen.blit(back,(backpos,-250))
    screen.blit(animation[int(animationnum)],bird[0].topleft)
    popcount=0
    for i in range(len(poles)):
        rect1=screen.blit(poleimgs[poles[i-popcount][0]][0],(poles[i-popcount][1],0))
        rect2=screen.blit(poleimgs[poles[i-popcount][0]][1],(poles[i-popcount][1],615-poleimgs[poles[i-popcount][0]][1].get_height()))
        if bird[rect].colliderect(rect1)or bird[rect].colliderect(rect2):
            screen.blit(gameover,(0,0))
            screen.blit(ScoreFont2.render("Score: "+str(bird[Score]) ,True,(0,255,0)),(330,590))
            display.flip()
            if topscore<bird[Score]:
                topscore=bird[Score]
            diary=open("diary.txt","w")
            diary.write(str(topscore)+"\n"+str(totalflaps))
            diary.close()
            time.delay(5000)
            quit()
            
        poles[i-popcount][1]-=2
        if poles[i-popcount][1]<75 and poles[i-popcount][2]==True:
            poles[i-popcount][2]=False
            bird[Score]+=1  
        elif poles[i-popcount][1]<-100:
            poles.pop(i)
            popcount+=1
    screen.blit(ScoreFont.render("Score: "+str(bird[Score]) ,True,(0,255,0)),(800,0))
    clock.tick(60)
    display.flip()
def physics(bird):
    if bird[Upkey]==True:
        bird[vy]=6
        bird[rect].y-=10
        bird[Onground]=False
    if bird[Onground]==False:
        if bird[vy]>-12:
            bird[vy]-=0.3
    else:
        bird[vy] = 0
    if bird[rect].y>595:
        bird[Onground]=True
        bird[rect].y+=bird[vy]
    if bird[Onground]== False:
        bird[rect].y-=bird[vy]
    return bird
def createpole(poles):
    poles.append([randint(0,5),1000,True])
    return poles
poles=[]
poleimgs=[[image.load(x)for x in glob.glob("poles/1/*.png")],[image.load(x)for x in glob.glob("poles/2/*.png")],[image.load(x)for x in glob.glob("poles/3/*.png")],[image.load(x)for x in glob.glob("poles/4/*.png")]
          ,[image.load(x)for x in glob.glob("poles/5/*.png")],[image.load(x)for x in glob.glob("poles/6/*.png")]]
while running:
    if spawnpoles==False:
        polesdelay+=1
        if polesdelay==200:
            spawnpoles=True
    elif spawnpoles==True:
        polespawner+=1
        if polespawner==200:
            polespawner=0
            createpole(poles)
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_UP:
                if bird[rect].y>0:
                    bird[Upkey]=True
                    totalflaps+=1
            if e.key == K_ESCAPE:
                paused=True
                screen.blit(pausescreen,(0,0))
                display.flip()
                while paused:
                    for e in event.get():
                        if e.type == KEYDOWN:
                            if e.key == K_ESCAPE:
                                paused=False
    bird = physics(bird)
    backpos-=2
    update(back,backpos,bird,animation,animationnum,poles,topscore,totalflaps)
    animationnum+=0.2
    if animationnum>=4:
        animationnum=0
    bird[Upkey]=False
