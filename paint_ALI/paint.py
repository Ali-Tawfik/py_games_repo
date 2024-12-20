#Ali Tawfik
#This is my paint program this program contains many
#tools like brush pencil select text etc
#it contains music, pictures, filters and backgrounds
# there is also an easter egg if you type far cry with the text tool 
from pygame import*
from random import*
from math import*
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import webbrowser
#OPERATIONS USED
#[image.load] allows user to load image from directory
init()#initilizes pygame
arc_flag=0#flag for arc
word=""#var used to blit the text on the screen
textpos=0#var used to show position on the typing line between the letters
cropside=""#which side is cropping when using crop tool
alphaval=10#value of the slider for alpha brush
tab_Rect=[]#list of the Rects for tabs
colortool=""#flag for if colour is one or two
colours=[(255,0,0,2),(0,200,0,3),(0,0,255,2),(155,0,155,3),(200,200,0,3)] #alpha colours to blit on the canvas
root = Tk() #Tk dialog box
root.withdraw()
music_Rect=[] #Rect of all music pictures
shape=0         #Tool shape flag
text_flag=0          #Tool text flag
select_flag=0        #Tool select flag
selecting=0        #Tool selecting flag
musicstat=0     #Tool flag
myClock = time.Clock()
mx,my=(0,0) #location of mouse at the begging
flags = FULLSCREEN #makes the screen fullscreen
trans=1 #if canvas is seethrough or not
tab=""      #tells you what tab you are on
tool=""     #TELLS THE CURRENT ACTIVE TOOL 
side_Rect=Rect(0,0,297,720)#makes rect for the side where tools are
selections=[]#what tools are avalable at current tab
tab_Rect=[]#Tabs (tools,pics,music)
screen = display.set_mode((1280,720))#creating the display 1280x720
#screen.fill((255,255,255))
display.set_caption("FarCry 4 Paint")
screen.fill((0,0,0))
#_____________BEGINING FADE IN__________________________________________
begin=image.load("begin.jpg").convert()#screen at beginning
logo=image.load("logo.png")#logo fade in and out
imagelist=[begin,logo]#list of the start screen pics
speedlist=[1,0.9]
poslist=[(0,0),(400,400)]
fonttype="Cooper Std Black"#font thats going to be used during the paint
def blit_alpha(target,image, location, opacity):#takes png and allows it to be blitted/faded with empty background using a Surface
        x = location[0]
        y = location[1]
        temp = Surface((image.get_width(), image.get_height())).convert()
        temp.blit(target,(-x, -y))
        temp.blit(image,(0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
def fadein(image,speed,pos):#takes image speed and pos and fades in an image
    skip=0
    for j in range(len(image)):
        for i in range(int(255/speed[j])):
            screen.fill((0,0,0))
            for evt in event.get():
                if evt.type==MOUSEBUTTONDOWN:
                    if evt.button==1:
                        skip=1              #checks if mouse is down so program can skip the fade in
                if evt.type==QUIT:
                    skip=1
            if skip==1:#breaks if mouse1 down
                   break
            for k in range(j):
                screen.blit(image[0],pos[0])
            blit_alpha (screen,image[j],pos[j],int(i*speed[j]))
            display.flip()
def fadeout(image,speed,pos):#takes image speed and pos and fades out an image
    for i in range(int(255/speed)):
        screen.blit(image,pos)
        image.set_alpha(int((255-i)*speed))
fadein(imagelist,speedlist,poslist)
### LOADING ALLL PICTURES_____________________
background=image.load("farcryback.jpg")
canvaspic=image.load("canvas.jpg")#950X600
save=image.load("save.png")
load=image.load("load.png")
info=image.load("info.png")
canvaspic.set_alpha(100)
tabs=[]
mouse.set_pos([600,500])
#____________TOOLS AND Spec___
musicpics=[]
for i in range (1,9):
   musicpics.append(image.load("music/pic"+str(i)+".jpg")) 

colorsspec=image.load("colors.png")#96x96
pencil=image.load("tools/pencil.png")#50x50
pencil=transform.scale(pencil,(50,50))
colorpicker=image.load("tools/colorpicker.png")
colorpicker=transform.scale(colorpicker,(50,50))#50x50
line=image.load("tools/line.png")#50x50
square=image.load("tools/square.png")#50x50
circle=image.load("tools/circle.png")#50x50
spray=image.load("tools/spray.png")#50x50
spray=transform.scale(spray,(50,50))#50x50
colorfill=image.load("tools/colorfill.png")#50x50
brush=image.load("tools/brush.png")#50x50
brush=transform.scale(brush,(50,50))#50x50
eraser=image.load("tools/eraser.png")#50x50
eraser=transform.scale(eraser,(50,50))#50x50
shapes=image.load("tools/shapetool.png")#
text=image.load("tools/text.png")#50x50
select=image.load("tools/select.png")#50x50
marker=image.load("tools/marker.png")#50x50
marker=image.load("tools/marker.png")#50x50
squareborder=image.load("tools/squaretools/border.png")#50x50
squarefill=image.load("tools/squaretools/squarefill.png")#50x50
color1=image.load("tools/squaretools/color1.png")
color2=image.load("tools/squaretools/color2.png")
move=image.load("tools/selecttools/move.png")
crop=image.load("tools/selecttools/crop.png")
resize=image.load("tools/selecttools/resize.png")
rotate=image.load("tools/selecttools/rotate.png")
duplicate=image.load("tools/selecttools/duplicate.png")
back=[]         #lists for loading more pictures in a better way 
backbox=[]
pic=[]
picbox=[]       #lists for loading more pictures in a better way 
#____________________________________BACKGROUNDS
easteregg=image.load("pics/easteregg.png")
for i in range (4):
    back.append(transform.scale(image.load("pics/back"+str(i+1)+".jpg"),(950,600)))
for i in range (4):
    backbox.append(transform.scale(back[i],(95,60)))
#_____________________________________PICS
for i in range (6):
    pic.append(transform.scale(image.load("pics/pic"+str(i+1)+".png"),(105,230)))
for i in range (6):
    picbox.append(transform.scale(pic[i],(90,175)))
#_____________________________________TABS
tools=image.load("tabs/tools.png")#90x30
pics=image.load("tabs/pics.png")#90x30
music=image.load("tabs/music.png")#90x30
exittab=image.load("tabs/exit2.png")#34X30
shapesoptions=0
def draw_select_options():  #blits the top for the select tool 
        list1=[]
        for x in range(315,676,90):  #blits empty squares at top
            draw.rect(screen,(255,255,255),(x,2,50,50))
            draw.rect(screen,(255,255,0),(x,2,50,50),5)
        list1.append(screen.blit(move,(315,2)))
        list1.append(screen.blit(resize,(405,2)))
        list1.append(screen.blit(crop,(495,2)))
        list1.append(screen.blit(rotate,(585,2)))
        list1.append(screen.blit(duplicate,(675,2)))
        return list1 #list1 returns the list of all the top rects for select
def draw_shape_options():#blits the top for the shape(square and circle) tool
        list1=[]
        for x in range(315,676,90):  #blits empty squares at top
            draw.rect(screen,(255,255,255),(x,2,50,50))
            draw.rect(screen,(255,255,0),(x,2,50,50),5)
        list1.append(screen.blit(color1,(315,2)))
        list1.append(screen.blit(color2,(405,2)))
        list1.append(screen.blit(squarefill,(495,2)))
        list1.append(screen.blit(squareborder,(585,2)))
        list1.append(screen.blit(square,(675,2)))
        return list1    #list1 returns the list of all the top rects for shape
def Fillpixels(list1,color,colorchange):    #Filles pixels inside an area for 
        while list1!=[]:
                fx,fy=list1.pop()
                colorlist1=screen.get_at((fx,fy))
                if colorlist1==color:   #checks if color is same as the colour pressed at the beggining
                        screen.set_at((fx,fy),Ali.color)
                        list1.append((fx+1,fy))
                        list1.append((fx-1,fy))
                        list1.append((fx,fy-1))
                        list1.append((fx,fy+1))
            
                                
class Drawer:# making a class for object Ali
    def __init__ (self,tool,tab,color,size,color2):
        self.tool = tool
        self.tab = tab
        self.color = color
        self.color2 = color2
        self.size = size
Ali=Drawer(None,None,(0,0,0,255),15,(255,255,0)) #making an object called Ali
running=1               #flags if program is still running or not
screen.blit(background,(0,0))
tabs.append(screen.blit(tools,(0,70)))                      #blitting the tabs and appending them to the tabs list so i can check if mouse collided later
tabs.append(screen.blit(pics,(90,70)))                      #|
tabs.append(screen.blit(music,(180,70)))                    #|
tabs.append(screen.blit(exittab,(270,70)))                  #blitting the tabs and appending them to the tabs list so i can check if mouse collided later
canvas=screen.blit(canvaspic,(300,70))                      #blits white canvas
draw.rect(screen,(255,255,0),(298,68,954,604),5)
def cleartop():#clears the top makes a rect and clips then blits the background
    screen.set_clip(Rect(0,0,1280,65))
    screen.blit(background,(0,0))
    screen.set_clip(None)
def Clearside(): #clears all the tools on the side
    tab=""
    tab_Rect=[]
    screen.blit(background,(0,0))
    screen.blit(tools,(0,70))
    screen.blit(pics,(90,70))
    screen.blit(music,(180,70))
    screen.blit(exittab,(270,70))
    screen.blit(canvaspic,(300,70))
    draw.line(screen,(255,255,0),(0,70),(300,70),5)
    draw.rect(screen,(255,255,0),(298,68,954,604),5)#border
    return(tab)
def Drawtools(tab_Rect):#draws all the tools on the side
    tab="tools"
    for x in range(10,220,90):#draws the squares
        for y in range(135,440,90):  
            draw.rect(screen,(255,255,255),(x,y,50,50))
            draw.rect(screen,(255,255,0),(x,y,50,50),5)
    draw.rect(screen,(255,255,255),(10,495,50,50))
    draw.rect(screen,(255,255,0),(10,495,50,50),5)
    #________________DRAWING AND STORING TOOL RECTS_______________
    pencil_Rect=screen.blit(pencil,(10,135))
    brush_Rect=screen.blit(brush,(10,225))
    eraser_Rect=screen.blit(eraser,(100,135))
    spray_Rect=screen.blit(spray,(190,135))
    colors_Rect=screen.blit(colorsspec,(20,600))
    draw.rect(screen,(255,255,0),(20,600,98,98),3)#colour rect
    colorpicker_Rect=screen.blit(colorpicker,(190,225))
    colorfill_Rect= screen.blit(colorfill,(100,225))
    alphaspec_Rect=draw.rect(screen,(255,255,255),(20,570,100,20))
    draw.line(screen,(235,100,5),((alphaval-1)*6+20,570),((alphaval-1)*6+20,590),3)
    draw.rect(screen,(255,255,0),(20,570,100,20),3)#rect
    square_Rect=screen.blit(square,(10,315))
    line_Rect=screen.blit(line,(100,315))
    circle_Rect=screen.blit(circle,(190,315))
    shapes_Rect=screen.blit(shapes,(10,405))
    text_Rect=screen.blit(text,(100,405))
    select_Rect=screen.blit(select,(190,405))
    marker_Rect=screen.blit(marker,(10,495))
    save_Rect=screen.blit(save,(3,3))
    load_Rect=screen.blit(load,(63,3))
    info_Rect=screen.blit(info,(123,3))
    tab_Rect=[]
    tab_Rect.append(brush_Rect)
    tab_Rect.append(eraser_Rect)
    tab_Rect.append(spray_Rect)
    tab_Rect.append(pencil_Rect)
    tab_Rect.append(colorfill_Rect)
    tab_Rect.append(colorpicker_Rect)
    tab_Rect.append(square_Rect)
    tab_Rect.append(line_Rect)
    tab_Rect.append(circle_Rect)
    tab_Rect.append(shapes_Rect)
    tab_Rect.append(text_Rect)
    tab_Rect.append(select_Rect)
    tab_Rect.append(marker_Rect)
    tab_Rect.append(alphaspec_Rect)
    tab_Rect.append(info_Rect)
    tab_Rect.append(save_Rect)
    tab_Rect.append(load_Rect)
    tab_Rect.append(colors_Rect)
    #__________________END_______________________________
    return(tab_Rect,tab)
def Drawmusic():    #drawing the music selections
    counter=0#to draw the music pics
    music_Rect=[]
    for x in range(10,189,100):
        for y in range(135,450,90):#draws the squares
            draw.rect(screen,(255,255,255),(x,y,100,100))
            draw.rect(screen,(255,255,0),(x,y,100,100),5)
            #if counter<=5:
            music_Rect.append(screen.blit(musicpics[counter],(x+5,y+5)))
            counter+=1
    return music_Rect
def Drawpics():
    tab_Rect=[]
    counter=0
    counter1=0
    counter2=0
    colours=[(255,0,0,80),(0,255,0,80),(0,0,255,80),(255,0,255,80),(255,255,0,120)]
    for x in range(10,200,90):
        for y in range(135,450,170):
            draw.rect(screen,(255,255,255),(x,y,100,175))
            draw.rect(screen,(255,255,0),(x,y,100,175),5)
            tab_Rect.append(screen.blit(picbox[counter1],(x,y)))
            counter1+=1
    #________________DRAWING AND STORING MUSIC RECTS_______________
    for x in range(300,900,140):
            draw.rect(screen,(255,255,255),(x,2,95,60))
            draw.rect(screen,(255,255,0),(x,2,95,60),5)
            screen.blit(backbox[0],(x,2))
            alpsurf=Surface((95,60),SRCALPHA)
            draw.rect(alpsurf,(colours[counter2]),(0,0,95,60))
            counter2+=1
            tab_Rect.append(screen.blit(alpsurf,(x,2)))
    for x in range(20,250,140):
        for y in range(530,630,80):
            draw.rect(screen,(255,255,255),(x,y,95,60))
            draw.rect(screen,(255,255,0),(x,y,95,60),5)
            tab_Rect.append(screen.blit(backbox[counter],(x,y)))
            counter+=1
    #__________________END_______________________________
    return(tab_Rect)
def Drawcircletool():#draws the circle to show color and size
    draw.rect(screen,(255,255,255),(150,600,100,100))
    draw.rect(screen,(255,255,0),(150,600,100,100),5)
    draw.circle(screen,Ali.color,(200,650),int(Ali.size))
def drawsquaretool():#draws the square to show thickness and colour
    draw.rect(screen,(255,255,255),(150,600,100,100))
    draw.rect(screen,(255,255,0),(150,600,100,100),5)
    draw.rect(screen,Ali.color,(185,630,40,40))
    draw.rect(screen,Ali.color2,(185,630,40,40),int(Ali.size))
def undo():#goes back one step
    
    if len(canvascopies)>1:
        canvasredos.append(canvascopies.pop(-1))
        screen.blit(canvascopies[-1],(300,70))
    elif len(canvascopies)==1:
        screen.blit(canvascopies[-1],(300,70))
def redo():#goes forward one step
    if len(canvasredos)>0:
        screen.blit(canvasredos[-1],(300,70))
        canvascopies.append(canvasredos.pop(-1))
subtool=""#represnts selected subtools like filled square empty square move rotate etc.
oldmx=0
canvascopies=[canvaspic]#list of all the canvas copies for undo()
canvasredos=[]#list of all the canvas copies for redo()
fpsfont=font.SysFont("Times New Roman",20)# text type for the FPS AT TO RIGHT
#_________________RUNNING__________________
while running==1:
    if text_flag==1 and word.lower()=="far cry":
        word=""
        text_flag=0
        screen.set_clip(canvas)
        screen.blit(screen_copy,(0,0))
        screen.blit(easteregg,(300,70))
        screen.set_clip(None)
    kb=key.get_pressed()#gets the status of mouse, mb[0]=right,mb[1]=mid,mb[2]=left
    if select_flag==1 and kb[K_BACKSPACE]:
        screen.set_clip(canvas)
        inside_surf.fill((255,255,255,0))
        screen.set_clip(None)
        select_flag=0
    if Ali.size<1:#ristricts the resize tool
        Ali.size=1
    if Ali.size>50:
        Ali.size=49
    screen.blit(tools,(0,70))#tabs bliting
    screen.blit(pics,(90,70))#"     "
    screen.blit(music,(180,70))#" "
    screen.blit(exittab,(270,70))#"  " 
    draw.line(screen,(255,255,0),(0,70),(300,70),5)#tabs bliting
    mouse1=0#detects if mouse is clicked or not
    mouse3=0#detects if mouse is unclicked
    keys=key.get_pressed()#gets pressed keys
    oldmx,oldmy=(mx,my)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    #Ali.color= screen.get_at((mx,my))
    #screen.set_clip(rectangle)

    
#___________________EVENTLOOP_______________________
    for evt in event.get():
        if evt.type==KEYDOWN:
            myfont=font.SysFont(fonttype,int(Ali.size)*3)#e
            #REDO AND UNDO____________________________________
            if kb[K_LCTRL] and evt.key==K_z:
                screen.set_clip(None)
                undo()
                text_flag=0
            if kb[K_LCTRL] and evt.key==K_y and canvasredos!=[]:#redo
                screen.set_clip(None)
                redo()
            if text_flag==1:
                screen.set_clip(canvas)
                if evt.key==K_RIGHT and textpos!=0:
                    textpos-=1
                if evt.key==K_LEFT:
                    textpos+=1
                letter=evt.unicode
                if kb[K_LCTRL] and evt.key==K_z:
                    letter=""
                if kb[K_LCTRL] and evt.key==K_y and canvasredos!=[]:#redo 
                    letter=""
                if evt.key==K_RETURN:
                    textpos=0
                    letter=""
                    screen.blit(screen_copy,(0,0))
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    screen_copy=screen.copy()
                    word=""
                    texty+=Ali.size*3
                screen.blit(screen_copy,(0,0))
                if textpos!=0:
                    if evt.key==K_BACKSPACE:#deleting the character after the (|) line
                        word=word[:-textpos-1]+word[-textpos:]
                        letter=""
                    word=word[:-textpos]+letter+"|"+word[-textpos:]
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    word=word[:-textpos-1]+word[-textpos:]
                elif textpos==0:
                    if evt.key==K_BACKSPACE:#deleting the last character of the sent text tool
                        letter=""
                        word=word[:-1]
                    word+=letter
                    word+="|"
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    word=word[:-1]
                screen.set_clip(None)
        if evt.type==MOUSEBUTTONUP:
            if evt.button==1:
                mouse3=1#var for if mouse is up/ unclicked
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                mouse1=1 #var for if mouse is clicked
                xold=mx#variable to represent mx from previous loop
                yold=my#variable to represent my from previous loop
            if evt.button==3:
                if tool=="shape":
                    if shape==1:
                        shape=0
                        undo()
            if evt.button==4:#scrolling up
                Ali.size+=0.5#increase tool size
                if text_flag==1:
                    myfont=font.SysFont(fonttype,int(Ali.size)*3)
                    if textpos!=0:
                        word=word[:-textpos]+letter+"|"+word[-textpos:]
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))
                        screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                        word=word[:-textpos-1]+word[-textpos:]
                    if textpos==0:
                        word+="|"
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))
                        screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                        word=word[:-1]
                    screen.set_clip(None)
                if tool == "square" or tool == "circle":
                    drawsquaretool()
                elif tab=="tools":
                    Drawcircletool()
            if evt.button==5:
                Ali.size-=0.5#decrease size of tools
                if text_flag==1:
                    myfont=font.SysFont(fonttype,int(Ali.size)*3)
                    if textpos!=0:
                        word=word[:-textpos]+letter+"|"+word[-textpos:]
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))
                        screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                        word=word[:-textpos-1]+word[-textpos:]
                    if textpos==0:
                        word+="|"
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))
                        screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                        word=word[:-1]
                    screen.set_clip(None)
                if tool == "square" or tool == "circle":
                    drawsquaretool()
                elif tab=="tools":
                    Drawcircletool()
        if evt.type==QUIT or keys[K_ESCAPE] :
            running=0#closes the program

  
#_____________________CHCKING MOUSE CLICK UP_________
    if mouse3==1:
        if tab == "music":
            for i in range (len(musiclist)):
                if music_Rect[i].collidepoint((mx,my)):
                    mixer.music.load(musiclist[i])
                    time.delay(100)
                    screen.set_clip(side_Rect)
                    Clearside()
                    music_Rect=Drawmusic()
                    screen.set_clip(None)
                    if musicstat==0:
                        draw.rect(screen,(230,60,10),(music_Rect[i].left-5,music_Rect[i].top-5,music_Rect[i].width+10,music_Rect[i].height),5)
                        mixer.music.play()
                        stat=fpsfont.render("Music: ON",1,(0,0,0))
                        draw.rect(screen,(255,255,255),(115,517,105,32))
                        screen.blit(stat,(120,520))
                        musicstat=1
                    else:
                        mixer.music.stop()
                        print("why")
                        stat=fpsfont.render("Music: OFF",1,(0,0,0))
                        draw.rect(screen,(255,255,255),(115,517,105,32))
                        screen.blit(stat,(120,520))
                        musicstat=0
        if tab!="" and canvas.collidepoint((mx,my)):
            if tool=="select" and select_flag==1 and subtool=="resize":
                inside_surf=newinside_surf
            if tool=="select" and select_flag==1 and subtool=="crop":
                cropsurf=Surface((rect_Rect.width,rect_Rect.height))
                if cropside=="right":
                    cropsurf.blit(inside_surf,(0,0))
                elif cropside=="left":
                    inside_Rect=inside_surf.get_rect()
                    cropsurf.blit(inside_surf,(-(inside_Rect.width-rect_Rect.width),-(inside_Rect.height-rect_Rect.height)))
                inside_surf=cropsurf
            if tool=="select" and select_flag==0:
                inside_surf=screen_copy.subsurface(rect_Rect).copy()
                select_flag=1
                draw.rect(screen_copy,(255,255,255),rect_Rect)
                rect_height=rect_Rect.height
                rect_width=rect_Rect.width
                rect_top=rect_Rect.top
                rect_left=rect_Rect.left
            elif select_flag==2:
                screen.set_clip(canvas)
                if subtool!="crop":
                    #inside_surf=transform.scale(inside_surf,(rect_Rect.width,rect_Rect.height))
                    screen.blit(screen_copy,(0,0))
                    screen.blit(inside_surf,(rect_Rect.left,rect_Rect.top))
                elif cropside=="right":
                    screen.blit(inside_surf,(rect_Rect.left,rect_Rect.top))
                elif cropside=="left":
                    inside_Rect=inside_surf.get_rect()
                    screen.blit(inside_surf,(rect_Rect.right-inside_Rect.width,rect_Rect.bottom-inside_Rect.height))
                screen_copy=screen.copy()
                canvascopies.append(screen.subsurface(canvas).copy())
                screen.set_clip(None)
                select_flag=0
            if tool=="select" and select_flag==1 and subtool=="rotate":
                select_flag=0
                shapeoptionRects=draw_select_options()#Rects for the subtools of shape tools
                draw.rect(screen,(0,0,255),shapeoptionRects[0],5)
            if tool!="" and tool!="select" and select_flag == 0:   #undos and redos
                canvascopies.append(screen.subsurface(canvas).copy())
                if canvasredos!=[]:
                    canvasredos=[]

        elif canvas.collidepoint((mx,my))==False and selecting==1 and tool=="select":
            screen.set_clip(canvas)
            screen.blit(screen_copy,(0,0))
            screen.set_clip(None)
        selecting=0#show they are no longer selecting with select tool
    if mouse1==1:
        if tool== "text" and text_flag==1:
            screen.set_clip(canvas)
            screen.blit(screen_copy,(0,0))
            screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
            screen.set_clip(None)
        if tool!="select" and canvas.collidepoint((mx,my)):
            screen_copy=screen.copy()
        #_____________MOuse click on canvas(aftercopy)______________________________________
        if select_flag==1 and rect_Rect.collidepoint((mx,my)) and subtool== "crop" and canvas.collidepoint((mx,my)):
                if mx<rect_Rect.centerx:
                        cropside="left"
                else:
                        cropside="right"
        for i in range(6):
            if tool=="pic"+str(i+1):
                pic_ang=0#angle for rotation of pictures

        if canvas.collidepoint((mx,my)):
            if tool== "text":
                myfont=font.SysFont(fonttype,int(Ali.size)*3)
                if text_flag==1:
                    word=""
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    screen.set_clip(None)
                canvascopies.append(screen.subsurface(canvas).copy())
                textx,texty=(mx,my-int(Ali.size*3/2))
                word="|"#starting new word
                screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                word=""
                text_flag=1
                
            startmx=mx
            startmy=my#tells where mouse was clicked
            if tool=="select":
                if select_flag==0:
                    selecting=1
                if select_flag!=1:
                    screen_copy=screen.copy()
                elif rect_Rect.collidepoint((mx,my)):
                   nothi=0#random var so it doesnt crash for now

                else:
                    select_flag=2

            if tool=="shape":
                if shape==1:
                    canvascopies.pop(-1)
                    canvascopies.append(screen.subsurface(canvas).copy())
                else:
                    shape=1
                    canvascopies.append(screen.subsurface(canvas).copy())

            if tool=="colorfill":
                color=screen.get_at((mx,my))
                Fillpixels([(mx,my)],color,Ali.color)
        elif tool!= "shape":
            startmx=0
            startmy=0   #setting START MX to 0 so square line and circle wont draw

        if tab=="tools" or tab=="pictures":
            if tool== "square"or tool=="circle" or tool=="select":
                for i in range (len(subselections)):
                    if shapeoptionRects[i].collidepoint((mx,my)):
                       if subselections[i]=="color1" or subselections[i]=="color2":
                               colortool= subselections[i]
                       elif subselections[i]=="duplicate":
                           if select_flag==1:
                               screen.set_clip(canvas)
                               screen.blit(inside_surf,(rect_Rect.left,rect_Rect.top))
                               screen.set_clip(None)
                               canvascopies.append(screen.subsurface(canvas).copy())
                               screen_copy=screen.copy()
                               screen.set_clip(canvas)
                               rect_Rect=screen.blit(inside_surf,(rect_Rect.left+5,rect_Rect.top+5)) 
                               draw.rect(screen,(0,0,0),rect_Rect,1)
                               screen.set_clip(None)
                       else:
                               oldsubtool=subtool#old tool so it can deactivate and check for certain things
                               subtool=subselections[i]#the tool of tools for example the select (move,rotate etc.)
                               if oldsubtool!=subtool:
                                       if tool=="select":
                                               shapeoptionRects=draw_select_options()
                                               draw.rect(screen,(0,0,255),shapeoptionRects[i],5)
                                       elif tool=="square"or tool=="circle":
                                               shapeoptionRects=draw_shape_options()
                                               draw.rect(screen,(0,0,255),shapeoptionRects[i],5)
                       if subselections[i]=="move" and select_flag==1:
                           rect_height=rect_Rect.height
                           rect_width=rect_Rect.width


                               
#_______________CHECKING THE collision with the Tool and picture rects
            for i in range (len(selections)):
                if tab_Rect[i].collidepoint((mx,my)):
                    if shape==1:
                        undo()
                        shape=0
                    text_flag=0#test tool on or off
                    oldtool=tool#old tool to check if you have to clear top
                    tool=selections[i]#new tool assined
                    if oldtool== "select" and select_flag==1:
                        select_flag=0
                        screen.set_clip(canvas) 
                        screen.blit(inside_surf,(rect_Rect.left,rect_Rect.top))
                        screen_copy=screen.copy()
                        screen.blit(screen_copy,(0,0))
                        screen.set_clip(None)
                    if tool=="square" or tool=="circle":
                        shapeoptionRects=draw_shape_options()
                        subselections=["color1","color2","filledsquare","borderonly","square"]#sub selections are options for shape tools
                        colortool="color2"#color tool is the color used when using shape tools
                    elif oldtool=="square" or oldtool=="circle"or oldtool=="select":
                        cleartop()
                        drawsquaretool()
                    if tool=="select":
                        shapeoptionRects=draw_select_options()
                        subselections=["move","resize","crop","rotate","duplicate"]#sub selections are options for the select tools
                        subtool="move"#first subtool option
                        draw.rect(screen,(0,0,255),shapeoptionRects[0],5)
                    if tab=="tools":
                        screen.set_clip(side_Rect)
                        Clearside()
                        Drawtools(tab_Rect)
                        trans == 0#if canvas is seethroiugh
                        screen.set_clip(None)
                        if tool=="square" or tool=="circle":
                                drawsquaretool()
                        else:
                                Drawcircletool()
                    elif tab== "pictures":
                        screen.set_clip(side_Rect)
                        Clearside()
                        Drawpics()
                        screen.set_clip(None)
                        trans == 0
                    draw.rect(screen,(230,60,10),tab_Rect[i],5) #drawing orange box
            if tab== "pictures":
                for i in range(4):
                    if tab_Rect[-4+i].collidepoint((mx,my))and tab== "pictures":
                        screen.blit(back[i],(300,70))
                        canvascopies.append(screen.subsurface(canvas).copy())
                for i in range(5):
                    if tab_Rect[6+i].collidepoint((mx,my))and tab== "pictures":
                        alpsurf=Surface((950,600),SRCALPHA)
                        draw.rect(alpsurf,(colours[i]),(0,0,950,600))
                        for i in range(50):
                            screen.blit(alpsurf,(300,70))
                        canvascopies.append(screen.subsurface(canvas).copy())
        if tab=="tools"and tab_Rect[-4].collidepoint((mx,my)):#
            webbrowser.open("help.py")#opens the help if clicked on info icon
        if tab=="tools"and tab_Rect[-3].collidepoint((mx,my)):#saveimage
            fileName = asksaveasfilename(parent=root,title="Save the image as...")
            image.save(screen.subsurface(canvas),fileName+".png")
        if tab=="tools"and tab_Rect[-2].collidepoint((mx,my)):#load image
            fileName = askopenfilename(parent=root,title="Open Image:")
            loadedpic=image.load(fileName)
            screen.set_clip(canvas)
            screen.blit(loadedpic,(300,70))
            screen.set_clip(None)
        if tab=="tools"and tab_Rect[-1].collidepoint((mx,my)): #color spectrum
            if tool !="square" and tool != "circle":
                Ali.color= screen.get_at((mx,my))
            if text_flag==1:
                if textpos!=0:
                    word=word[:-textpos]+letter+"|"+word[-textpos:]
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    word=word[:-textpos-1]+word[-textpos:]
                if textpos==0 and tool=="text":
                    word+="|"
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    screen.blit(myfont.render(word,int(Ali.size),Ali.color),(textx,texty))
                    word=word[:-1]
                screen.set_clip(None)
            if tool == "square" or tool == "circle":
                if colortool== "color1":
                    Ali.color= screen.get_at((mx,my))
                elif colortool== "color2":
                    Ali.color2= screen.get_at((mx,my))
                drawsquaretool()
            else:
                 Drawcircletool()



                 
#_________________CHCKING TAB COLLIDE_______________________
        if tabs[0].collidepoint((mx,my)): #toolcollide
            if trans == 1:
                canvaspic.set_alpha(255)
                screen.blit(canvaspic,(300,70))
            cleartop()
            screen.set_clip(side_Rect)
            Clearside()
            tab_Rect,tab=Drawtools(tab_Rect)
            Drawcircletool()
            selections=["brush","eraser","spray","pencil","colorfill","colorpicker","square","line","circle","shape","text","select","marker",]
            screen.set_clip(None)
            trans = 0
        if tabs[1].collidepoint((mx,my)):#picture collide
            if trans == 1:
                canvaspic.set_alpha(255)
                screen.blit(canvaspic,(300,70))
            screen.set_clip(side_Rect)
            selections=["pic1","pic2","pic3","pic4","pic5","pic6"]
            subselections=[]
            Clearside()
            cleartop()
            tab_Rect=Drawpics()
            screen.set_clip(None)
            tab="pictures"
            trans = 0
        if tabs[2].collidepoint((mx,my)): #musiccollide
            if trans == 1:
                canvaspic.set_alpha(255)
                screen.blit(canvaspic,(300,70))
            canvaspic.set_alpha(255)
            screen.set_clip(side_Rect)
            Clearside()
            cleartop()
            music_Rect=Drawmusic()
            subselections=[]
            tab="music"#tells what tab is active
            screen.set_clip(None)
            trans = 0
            musiclist=[]
            for i in range (1,9):
                musiclist.append("music/music"+str(i)+".mp3")
        if tabs[3].collidepoint((mx,my)):#exit collide
            canvaspic.set_alpha(100)
            tool=""
            tab=Clearside()
            cleartop()
            trans=1
            canvascopies=[canvaspic]
            subselections=[]
            canvasredos=[]
            shape=0
            tab_Rect=[]
            selections=[]
    if tab=="tools"and tab_Rect[-5].collidepoint((mx,my)) and mb[0]==1:#alpha value editor
            draw.rect(screen,(255,255,255),(20,570,100,20))
            draw.line(screen,(235,100,5),(mx,570),(mx,590),3)
            draw.rect(screen,(255,255,0),(20,570,100,20),3)#rect
            alphaval=int((mx-20)/6)+1
#______________________________Drawing PICTURE to canvas_________________
                
    if canvas.collidepoint((mx,my)):
        if tool=="shape" and shape==1:
            screen.set_clip(canvas)
            screen.blit(screen_copy,(0,0))
            dist=hypot(startmx-mx,startmy-my)#dist from the two points so circls can be drawn
            if dist==0:
                    dist=1
            incy=dist/dist*(my-startmy)/dist
            incx=dist/dist*(mx-startmx)/dist
            for i in range (int(dist)):
                    draw.circle(screen,Ali.color,(int(startmx),int(startmy)),int(Ali.size))
                    startmx+=incx
                    startmy+=incy
            startmx-=int(incx*dist)
            startmy-=int(incy*dist)
            screen.set_clip(None)
        if mb[0]==1 and mouse3!=1:


                
            
        #___________________________mouse on canvas and down (DRAWING)____    
            
            for i in range(6):
                if tool=="pic"+str(i+1)and startmx!=0:
                    kb=key.get_pressed()
                    if kb[K_RIGHT]:
                        pic_ang-=2#turning the pic right
                    if kb[K_LEFT]:
                        pic_ang+=2#turning the pic left
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    width=int(105*Ali.size/15)
                    lenght=int(230*Ali.size/15)
                    New_pic=transform.scale(pic[i],(width,lenght))
                    New_pic=transform.rotate(New_pic,pic_ang)
                    New_pic_Rect = New_pic.get_rect()
                    New_pic_Rect.center = (mx,my)
                    screen.blit(New_pic,New_pic_Rect)
                    screen.set_clip(None)

            if tool=="select" and startmx!=0:#select tool
                if select_flag==0 and subtool=="rotate":
                    subtool="move"
                    cleartop()
                    shapeoptionRects=draw_select_options()#rects for the top subtools for select tool
                    draw.rect(screen,(0,0,255),shapeoptionRects[0],5)
                if select_flag==0 and mouse3!=1:
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    rect_Rect=draw.rect(screen,(0,0,0),(startmx,startmy,mx-startmx,my-startmy),2)
                    screen.set_clip(None)
                if select_flag==1 and rect_Rect.collidepoint((mx,my)) and subtool=="move":
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    movex,movey=(mx-oldmx,my-oldmy)
                    rect_Rect.move(movex,movey)
                    screen.blit(inside_surf,(rect_Rect.left+movex,rect_Rect.top+movey))       #bliting the surface we got at mouse3
                    rect_Rect=draw.rect(screen,(0,0,0),(rect_Rect.left+movex,rect_Rect.top+movey,rect_width,rect_height),2)
                    screen.set_clip(None)
                if select_flag==1 and rect_Rect.collidepoint((mx,my)) and subtool== "resize" and canvas.collidepoint((mx,my)):
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    newinside_surf=transform.scale(inside_surf,(rect_Rect.width-(oldmx-mx),rect_Rect.height-(oldmy-my)))
                    screen.blit(newinside_surf,(rect_Rect.left,rect_Rect.top))       #bliting the surface we got at mouse3
                    rect_Rect=draw.rect(screen,(0,0,0),(rect_Rect.left,rect_Rect.top,rect_Rect.width-(oldmx-mx)-1,rect_Rect.height-(oldmy-my)-1),2)
                    screen.set_clip(None)
                if select_flag==1 and rect_Rect.collidepoint((mx,my)) and subtool== "crop" and canvas.collidepoint((mx,my)):
                    if cropside=="left":
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))#bliting the surface we got at mouse3
                        screen.set_clip(rect_Rect)
                        inside_Rect=inside_surf.get_rect()
                        screen.blit(inside_surf,(rect_Rect.right-inside_Rect.width,rect_Rect.bottom-inside_Rect.height))
                        screen.set_clip(canvas)
                        rect_Rect=draw.rect(screen,(0,0,0),(rect_Rect.left-(oldmx-mx),rect_Rect.top-(oldmy-my),rect_Rect.width-(mx-oldmx)-1,rect_Rect.height-(my-oldmy)-1),2)
                        screen.set_clip(None)
                    if cropside=="right":
                        screen.set_clip(canvas)
                        screen.blit(screen_copy,(0,0))#bliting the surface we got at mouse3
                        screen.set_clip(rect_Rect)
                        screen.blit(inside_surf,(rect_Rect.left,rect_Rect.top))
                        screen.set_clip(canvas)
                        rect_Rect=draw.rect(screen,(0,0,0),(rect_Rect.left,rect_Rect.top,rect_Rect.width-(oldmx-mx)-1,rect_Rect.height-(oldmy-my)-1),2)
                        screen.set_clip(None)
                if select_flag==1 and subtool== "rotate" and canvas.collidepoint((mx,my)):
                    screen.set_clip(canvas)
                    rotatesurf=Surface((rect_Rect.width+2,rect_Rect.height+2),SRCALPHA)
                    rotatesurf.blit(inside_surf,(1,1))
                    screen.blit(screen_copy,(0,0))
                    angle = atan2(rect_Rect.centerx-mx,rect_Rect.centery-my) * 180/pi
                    newinside_surf = transform.rotate(rotatesurf,angle)
                    newinside_Rect = newinside_surf.get_rect()
                    newinside_Rect.center = (rect_Rect.center)
                    screen.blit(newinside_surf,newinside_Rect)       #bliting the surface we got at mouse3
                    screen.set_clip(None)
            if tool=="marker" and mx!=oldmx or tool=="marker" and my!=oldmy:
                screen.set_clip(canvas)
                colour_list=list(Ali.color)
                colour_list[-1]=alphaval
                dist=hypot(oldmx-mx,oldmy-my)
                if dist==0:
                    dist=1
                incy=dist/(dist)*(my-oldmy)/dist
                incx=dist/(dist)*(mx-oldmx)/dist
                for i in range (int(dist)):
                    highlightsurface=Surface((int(Ali.size)*2,int(Ali.size)*2),SRCALPHA)
                    draw.circle(highlightsurface,tuple(colour_list),(int(Ali.size),int(Ali.size)),int(Ali.size))
                    screen.blit(highlightsurface,(oldmx-int(Ali.size),oldmy-int(Ali.size)))
                    oldmx+=incx
                    oldmy+=incy
                screen.set_clip(None)
            if tool=="square" and startmx!=0:
                square_Rect=Rect(startmx,startmy,mx-startmx,my-startmy)
                square_Rect.normalize()                                         #SQUARE
                if subtool=="filledsquare" and square_Rect.width//2> Ali.size and square_Rect.height//2 > Ali.size:
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    draw.rect(screen,Ali.color2,square_Rect)
                    draw.rect(screen,Ali.color,(square_Rect.left+Ali.size,square_Rect.top+Ali.size,square_Rect.width-Ali.size*2,square_Rect.height-Ali.size*2))
                    screen.set_clip(None)
                elif subtool=="borderonly"and square_Rect.width//2> Ali.size and square_Rect.height//2 > Ali.size:
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    squaresurf=Surface((square_Rect.width,square_Rect.height),SRCALPHA)
                    draw.rect(squaresurf,Ali.color2,(0,0,square_Rect.width,square_Rect.height))
                    draw.rect(squaresurf,(255,255,255,0),(0+Ali.size,0+Ali.size,square_Rect.width-Ali.size*2,square_Rect.height-Ali.size*2))
                    screen.blit(squaresurf,(square_Rect.left,square_Rect.top))
                    screen.set_clip(None)
                elif subtool=="square":
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    draw.rect(screen,Ali.color,(startmx,startmy,mx-startmx,my-startmy))
                    screen.set_clip(None)
                else:
                    
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    draw.rect(screen,Ali.color2,(startmx,startmy,mx-startmx,my-startmy))
                    screen.set_clip(None)
            if tool=="line"and startmx!=0:                    #LINE
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    dist=hypot(startmx-mx,startmy-my)
                    if dist==0:#dist then draws circle for every pixel
                            dist=1
                    incy=dist/dist*(my-startmy)/dist
                    incx=dist/dist*(mx-startmx)/dist
                    for i in range (int(dist)):
                            draw.circle(screen,Ali.color,(int(startmx),int(startmy)),int(Ali.size))
                            startmx+=incx
                            startmy+=incy
                    startmx-=int(incx*dist)
                    startmy-=int(incy*dist)
                    screen.set_clip(None)
            if tool=="circle"and startmx!=0:                  #CIRCLE
                circlerect=Rect(mx,my,startmx-mx,startmy-my)
                circlerect.normalize()
                if subtool=="filledsquare":
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    draw.ellipse(screen,Ali.color,circlerect)
                    if int(Ali.size) > circlerect.width//2 or int(Ali.size) > circlerect.height//2 :
                        draw.ellipse(screen,Ali.color2,circlerect)
                    else:
                        draw.ellipse(screen,Ali.color2,circlerect)
                        draw.ellipse(screen,Ali.color,(circlerect.left+Ali.size,circlerect.top+Ali.size,circlerect.width-Ali.size*2,circlerect.height-Ali.size*2))
                    screen.set_clip(None)
                elif subtool=="borderonly":
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    if int(Ali.size) > circlerect.width//2 or int(Ali.size) > circlerect.height//2 :
                        draw.ellipse(screen,Ali.color2,circlerect)
                    else:
                        circlesurf=Surface((circlerect.width,circlerect.height),SRCALPHA)
                        draw.ellipse(circlesurf,Ali.color2,(0,0,circlerect.width,circlerect.height))
                        draw.ellipse(circlesurf,(255,255,255,0),(0+Ali.size,0+Ali.size,circlerect.width-Ali.size*2,circlerect.height-Ali.size*2))
                        screen.blit(circlesurf,(circlerect.left,circlerect.top))
                    screen.set_clip(None)
                else:
                    screen.set_clip(canvas)
                    screen.blit(screen_copy,(0,0))
                    draw.ellipse(screen,Ali.color,circlerect)
                    screen.set_clip(None)
            if tool== "spray":
                screen.set_clip(canvas)
                for i in range(int(Ali.size)):
                    xspray=randint(-int(Ali.size),int(Ali.size))
                    yspray=randint(-int(Ali.size),int(Ali.size))
                    dist=hypot(xspray,yspray)
                    if dist< Ali.size:
                        screen.set_at((int(xspray)+mx,int(yspray)+my),Ali.color)
                screen.set_clip(None)
            if tool== "brush":
                screen.set_clip(canvas)
                dist=hypot(oldmx-mx,oldmy-my)
                if dist==0:
                    dist=1
                incy=dist/(dist)*(my-oldmy)/dist
                incx=dist/(dist)*(mx-oldmx)/dist
                for i in range (int(dist)):#dist then draws circle for every pixel
                    draw.circle(screen,Ali.color,(int(oldmx),int(oldmy)),int(Ali.size))
                    oldmx+=incx
                    oldmy+=incy
                screen.set_clip(None)
            if tool== "eraser":
                screen.set_clip(canvas)
                dist=hypot(oldmx-mx,oldmy-my)
                if dist==0: #dist then draws circle for every pixel
                    dist=0.001
                incy=dist/100*(my-oldmy)/dist
                incx=dist/100*(mx-oldmx)/dist
                for i in range (100):
                    draw.circle(screen,(255,255,255),(int(oldmx),int(oldmy)),int(Ali.size))
                    oldmx+=incx
                    oldmy+=incy
                screen.set_clip(None)
            if tool== "pencil":
                screen.set_clip(canvas)
                draw.line(screen,Ali.color,(oldmx,oldmy),(mx,my),1)
                (None)
            if tool== "colorpicker":
                Ali.color= screen.get_at((mx,my))
                Drawcircletool()
    display.flip()
    myClock.tick(60)
    fps=fpsfont.render(str(myClock.get_fps()),1,(0,0,0))  #Renders the FPS SPEED
    fps_RECT=draw.rect(screen,(255,255,255),(1260,0,20,20))#draws the rect for fps speed
    screen.set_clip(fps_RECT)
    screen.blit(fps,(1260,0))#Showes user FPS
    screen.set_clip(None)
quit()
