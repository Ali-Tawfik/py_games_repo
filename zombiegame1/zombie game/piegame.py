from pygame import*
from random import*
from math import*
init()
screen=display.set_mode((1000,650))
pistolsound = mixer.Sound("sound/pistol.wav")
bullethit= mixer.Sound("sound/bullethit.wav")
zombiedieing= mixer.Sound("sound/zombiedieing.wav")
zombiebitesound = mixer.Sound("sound/bite.wav")
zomspawnsound = mixer.Sound("sound/zombie spawn.wav")
player=image.load("character/playerpistol1.png")
playerpistolshot=image.load("character/playerpistolshoot.png")
start=image.load("start/start.png")
Map=image.load("map1.png")
Map.convert()
startbox=image.load("start/startbox.png")
quitbox=image.load("start/quitbox.png")
gameover=image.load("gameover.png")
reload_pic=image.load("elements/reload.png")
zombie1=[]
zombie2=[]
for i in range(8):
    zombie=image.load("zombies/zombie(1)"+str(i)+".png")
    zombie1.append(zombie)
for i in range(8):
    zombie=image.load("zombies/zombie(2)"+str(i)+".png")
    zombie2.append(zombie)
display.set_caption("ZOMBIES")
myClock = time.Clock()
class Player:
    def __init__ (self,hp,dmg,typ,typspeed,speed):
        self.hp = hp
        self.dmg = dmg
        self.typ = typ
        self.typspeed= typspeed
        self.speed= speed

class Zombie:
    def __init__(self,hp,dmg,speed,x,y,hits,frame,zomtype):
        self.hp = hp
        self.dmg = dmg
        self.speed = speed
        self.x = x
        self.y = y
        self.hits = hits       
        self.frame=frame
        self.zomtype=zomtype
class Bullet:
    def __init__(self,loc):
        self.loc=loc
game=1
while game==1:
    mixer.music.load("sound/intro.mp3")
    mixer.music.play()
    mappos=[-2000,-1300]
    screen.fill((0,255,0))
    Ali= Player(100,50,"gun",30,3)
    zomlist=[]
    xin=randint(0,1000)
    #zomb=Zombie(20,10,3,xin,0,100,0,1)
    #zomlist.append(zomb)
    spawnrate=150
    bullist=[]
    running=1
    zomspr=0
    reload=7
    shotsprt=1
    reloaddelay=50
    run=1
#_______________________START SCREEN________________________________________
    while run==1:
        screen.blit(start,(0,0))
        startcollide=screen.blit(startbox,(770,65))
        mx,my=mouse.get_pos()
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN and startcollide.collidepoint(mx,my):
                running=1
                mixer.music.stop()
                run=0
        display.update()
#______________________GAME RUNNING______________________________________
    while running==1:
        direction="none"
        keys=key.get_pressed()
        if keys[K_w]:
            mappos[1]+=Ali.speed
        if keys[K_s]:
            mappos[1]-=Ali.speed
        if keys[K_d]:
            mappos[0]-=Ali.speed
        if keys[K_a]:
            mappos[0]+=Ali.speed
        if spawnrate>60:
            spawnrate/=1.0001
        bulletx,bullety=950,575#start location for reload
        removed=0 #Checks how many zombies i removed
        fire=0 #checks For a click
    #_________________________ EVENTS LOOP __________________________
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN and reloaddelay==50:
                if reload>0:
                    fire=1
                    reload-=1
            if evt.type==KEYDOWN:
                if evt.key==K_r:
                    if reload==0:
                        reloaddelay=0
                    reloaddelay=0
                    reload=0
            if evt.type==QUIT:
                running=0
    #_________________KEY CHECKING AND SCREEN FILL__________________________
        if keys[K_r]and reloaddelay<50:
            reloaddelay+=1
            if reloaddelay==50:
                reload=7
        Map_Rect=screen.blit(Map,(mappos[0],mappos[1]))
    #________________________DRAWING BULLETS LEFT AND BARS__________________________
        for i in range (reload):
            draw.circle(screen,(255,255,0),(bulletx,bullety),25)
            bullety-=75
        if reload == 0:
            screen.blit(reload_pic,(140,595))
        draw.rect(screen,(255,255,255),(20,595,110,30))
        draw.rect(screen,(0,0,0),(25,600,reloaddelay*2,20))
        draw.rect(screen,(255,0,0),(0,20,Ali.hp*10,20))
    #________________________ GETTING AND BLITTING BOB ________________________________________________
        if Ali.typ == "bar":
            print("jo")
        elif Ali.typ == "gun":
            mb=mouse.get_pressed()
            mx,my=mouse.get_pos()
            deltaY = 325 - my
            deltaX = 500 - mx
            angle= atan2(deltaX,deltaY) * 180/pi
            player_imgNew=transform.rotate(player,angle)
            if shotsprt <1:
                shotsprt+=0.2
                player_imgNew=transform.rotate(playerpistolshot,angle)
            player_rectNew=player_imgNew.get_rect()
            player_rectNew.center = (500,325)
            ALI=screen.blit(player_imgNew,player_rectNew)#BOB MY AWESOMELY ANIMATED CHARACTER
            spawn=randint(0,int(spawnrate))
    #________________________________SPAWNING__________________________________
            if spawn==0:
                zomtype=randint(1,2)
                top_bot=randint(0,1)          #top or bottem spawn
                right_left=randint(0,1)
                if top_bot==1 and right_left==1:
                    yin=0
                    xin=randint(0,1000)
                if top_bot==1 and right_left==0:
                    yin=randint(0,1000)
                    xin=1000
                if top_bot==0 and right_left==1:
                    yin=750
                    xin=randint(0,1000)
                if top_bot==0 and right_left==0:
                    yin=randint(0,1000)
                    xin=0
                if zomtype == 1:
                    zomb=Zombie(20,1,2,xin,yin,100,0,zomtype)
                elif zomtype == 2:
                    zomb=Zombie(10,1,3,xin,yin,100,0,zomtype)
                zomlist.append(zomb)
    #________________________________ZOMBIE BLIT AND MOVEMENT__________________________________
            for i in range(len(zomlist)):
                i-=removed
                if keys[K_w]:
                    zomlist[i].y+=Ali.speed
                if keys[K_s]:
                    zomlist[i].y-=Ali.speed
                if keys[K_d]:
                    zomlist[i].x-=Ali.speed
                if keys[K_a]:
                    zomlist[i].x+=Ali.speed
                if zomlist[i].hits<100:
                    zomlist[i].hits+=1
                if zomlist[i].x != 425 and zomlist[i].y != 300:
                    zomlist[i].frame+=0.1
                if zomlist[i].frame>=8:
                    zomlist[i].frame=0
                dist=sqrt((450+30-zomlist[i].x)**2+(275+30-zomlist[i].y)**2)
                                        #ANGLE OF ZOMBIE
                ang= atan2(425+30 -zomlist[i].x ,275+30 - zomlist[i].y) * 180/pi
                if zomlist[i].zomtype==1:
                    zombtran=transform.rotate(zombie1[int(zomlist[i].frame)],ang)
                elif zomlist[i].zomtype==2:
                    zombtran=transform.rotate(zombie2[int(zomlist[i].frame)],ang)
                zomlist[i].x=-zomlist[i].speed/dist*(zomlist[i].x-425-30)+zomlist[i].x
                zomlist[i].y=-zomlist[i].speed/dist*(zomlist[i].y-275-30)+zomlist[i].y
                zomb_loc=zombtran.get_rect()
                zomb_loc.center = (500,325)
                collide=screen.blit(zombtran,(zomlist[i].x,zomlist[i].y))
                if zomlist[i].hits==100 and zomlist[i].x < 475 and zomlist[i].x > 375 and zomlist[i].y>260 and zomlist[i].y<340:
                    Ali.hp-=10
                    zombiebitesound.play()
                    zomlist[i-removed].hits=0
                    if Ali.hp==0:
                        running=0
    #______________________________________BULLET SPAWNING__________________________________________________________________________
                for k in bullist:
                    if collide.collidepoint(k[0],k[1]):
                        bullist.remove(k)
                        zomlist[i].hp-=10
                        zomlist[i].speed-=1
                        bullethit.stop()
                        bullethit.play()
                        if zomlist[i].hp <= 0:
                            zombiedieing.stop()
                            zombiedieing.play()
                            zomlist.pop(i)
                            removed+=1
            if fire==1:
                shotsprt=0
                pistolsound.stop()
                pistolsound.play()
                dist=hypot(mx-500,my-325)
                start_bully=30*(my-325)/dist
                start_bullx=30*(mx-500)/dist
                bully=10*(my-325)/dist
                bullx=10*(mx-500)/dist
                bullist.append([500+start_bullx,325+start_bully,bullx,bully])
            for i in bullist:
                i[0] += i[2]
                i[1] += i[3]
                if keys[K_w]:
                    i[1]+=Ali.speed
                if keys[K_s]:
                    i[1]-=Ali.speed
                if keys[K_d]:
                    i[0]-=Ali.speed
                if keys[K_a]:
                    i[0]+=Ali.speed
                bullet=draw.circle(screen,(255,255,0),(int(i[0]),int(i[1])),3)
            display.update()
            myClock.tick(60)
    play=1
    while play==1:
        screen.blit(gameover,(0,0))
        game_start=screen.blit(startbox,(100,550))
        game_quit=screen.blit(quitbox,(650,550))
        mx,my=mouse.get_pos()
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN and game_start.collidepoint(mx,my):
                running=1
                game=1
                play=0
            elif evt.type==MOUSEBUTTONDOWN and game_quit.collidepoint(mx,my):
                play=0
                game=0
            if evt.type==QUIT:
                play=0
                game=0
        display.update()
        myClock.tick(60)
quit()
