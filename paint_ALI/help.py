from pygame import*
import webbrowser
discription=[["This is a Pencil:","A pencil is used for writing on the","canvas. You can use a pencil by","selecting the pencil icon and holding","down the left button on the canvas."],
             ["This is an Eraser:","An eraser is used to erase the canvas.","You can use an eraser by selecting it and","holding down the left button on the","canvas."],
             ["This is a Spray can:","With this tool you can spray piant","your canvas. You can do so by selecting the","icon and holding down the left button","on the canvas."],
             ["This is a Brush:","A brush is used for drawing on the","canvas. You can use a brush by selecting","the Brush icon and holding down the","left button on the canvas."],
             ["This is a Filltool:","A fill is used for filling an area inside a","shape. You can use a Fill by selecting","the fill icon and clicking the left","button inside the area you want to","recolour."],
             ["This is a Colourpicker:","A picker is used for changing the colour.","You can use a picker by selecting","the picker icon and clicking the left","button on the colour you want to use."],
             ["This is a Square:","A squaretool is used for drawing","squares on the canvas. A square","contains 5 subtools, 2 for selecting","colours and 3 others for selecting the","format of the square you can use the","tool by clicking and draging the mouse."],
             ["This is a Line:","A linetool is used for drawing lines","on a canvas. You can use a line tool","by selecting the icon then clicking"," and draging the mouse on the canvas."],
             ["This is a Circle:","A circletool is used for drawing","circles on the canvas. A circle","contains 5 subtools, 2 for selecting","colours and 3 others for selecting the","format of the circle you can use the","tool by clicking and draging the mouse."],
             ["This is a Polygon tool:","The polygon tool is used for","drawing shapes with lines. to use","this tool click on the canvas and", "click again to make a line from old","to the new click position. when","done simply click the right button"],
             ["This is a Text tool:","The text tool is used to write","on the canvas. To use this tool","click on the canvas and type."],
             ["This is a Select tool:","The select tool is used to select","a portion of the canvas.","to select a portion just simply","hold and drag the mouse."],
             ["This is a Marker tool:","The Marker tool is used to paint","on the canvas. Click and","hold mouse down."],
             ["This is an Alpha slider:","Slide the orange line to change","alpha value of the marker."],
             ["This is a Colour spectrum:","Click on the colour spectrum","to change your color."],
             ["This is a Circle preview:","Circle preview shows the size and","colour of the user."],
             ["This is a Square preview:","Square preview is an alternate for","circle preview when using the shapes.","Square preview shows the size of the","border and the colour of the inside"," and outside of the square/circle."],
             ["This is the save icon:","to save a picture of a canvas click the","icon and save the picture"],
             ["This is the load icon:","to load a picture to the canvas click the","icon and save the picture"],
             ["This is a move subtool: (select)","after using select tool to select","an area click and hold mouse inside","the area to move the selected area"],
             ["This is a resize subtool: (select)","after using select tool to select","an area click and hold mouse inside","the area to resize the selected area"],
             ["This is a crop subtool: (select)","after using select tool to select","an area click and hold mouse inside","the area to crop the selected area"],
             ["This is a rotate subtool: (select)","after using select tool to select","an area click and hold mouse inside","the area to rotate the selected area"],
             ["This is a duplicate subtool: (select)","after using select tool to select","an area click on the icon to create","a copy of the selected area"],
             ["Colour 1 is a subtool of (shapes)","colour 1 controls the inside","of shapes. To change colour1","select the icon then select","the colour you want from the spectrum"],
             ["Colour 2 is a subtool of (shapes)","colour 2 controls the border","of shapes. To change colour12","select the icon then select","the colour you want from the spectrum"],
             ["This is a Filledshape subtool: (shapes)","draws a square that has a border","and is filled."],
             ["This is a border subtool: (shapes)","draws a square that has a border","and is not filled."],
             ["This is a plain subtool: (shapes)","draws a square that has no border","and is filled."],
             ]
screen = display.set_mode((700,700))
init()
running=True
def Drawcircletool():
    Rect=draw.rect(screen,(255,255,255),(120,600,100,100))
    draw.rect(screen,(255,255,0),(120,600,100,100),5)
    draw.circle(screen,(0,0,0),(170,650),10)
    return Rect
def drawsquaretool():
    Rect=draw.rect(screen,(255,255,255),(220,600,100,100))
    draw.rect(screen,(255,255,0),(220,600,100,100),5)
    draw.rect(screen,(0,0,0),(255,630,40,40))
    draw.rect(screen,(100,0,0),(255,630,40,40),10)
    return Rect
def Clearside():
    tab=""
    tab_Rect=[]
    draw.line(screen,(255,255,0),(0,70),(300,70),5)
    draw.rect(screen,(255,255,0),(298,68,954,604),5)#border
    return(tab)
side_Rect=Rect(0,0,297,720)
tools=image.load("tabs/tools.png")#90x30
pics=image.load("tabs/pics.png")#90x30
music=image.load("tabs/music.png")#90x30
exittab=image.load("tabs/exit2.png")#34X30
helpback=image.load("helpbackground.png")
colorsspec=image.load("colors.png")#96x96
pencil=image.load("tools/pencil.png")#47x47
pencil=transform.scale(pencil,(50,50))
colorpicker=image.load("tools/colorpicker.png")
colorpicker=transform.scale(colorpicker,(50,50))
line=image.load("tools/line.png")
square=image.load("tools/square.png")
circle=image.load("tools/circle.png")
spray=image.load("tools/spray.png")
spray=transform.scale(spray,(50,50))
colorfill=image.load("tools/colorfill.png")
brush=image.load("tools/brush.png")
brush=transform.scale(brush,(50,50))
eraser=image.load("tools/eraser.png")#47x47
eraser=transform.scale(eraser,(50,50))
shapes=image.load("tools/shapetool.png")#
text=image.load("tools/text.png")
save=image.load("save.png")
load=image.load("load.png")
select=image.load("tools/select.png")
marker=image.load("tools/marker.png")
moreinfo=image.load("tabs/moreinfo.png")
squareborder=image.load("tools/squaretools/border.png")
squarefill=image.load("tools/squaretools/squarefill.png")
color1=image.load("tools/squaretools/color1.png")
color2=image.load("tools/squaretools/color2.png")
move=image.load("tools/selecttools/move.png")
crop=image.load("tools/selecttools/crop.png")
resize=image.load("tools/selecttools/resize.png")
rotate=image.load("tools/selecttools/rotate.png")
duplicate=image.load("tools/selecttools/duplicate.png")
myfont=font.SysFont("Times New Roman",15)
def Drawtools():
    tab="tools"
    for x in range(10,220,90):#draws the squares
        for y in range(135,440,90):  
            draw.rect(screen,(255,255,255),(x,y,50,50))
            draw.rect(screen,(255,255,0),(x,y,50,50),5)
    draw.rect(screen,(255,255,255),(10,495,50,50))
    draw.rect(screen,(255,255,0),(10,495,50,50),5)
    pencil_Rect=screen.blit(pencil,(10,135))
    brush_Rect=screen.blit(brush,(10,225))
    eraser_Rect=screen.blit(eraser,(100,135))
    spray_Rect=screen.blit(spray,(190,135))
    colors_Rect=screen.blit(colorsspec,(20,600))
    draw.rect(screen,(255,255,0),(20,600,98,98),3)#colour rect
    colorpicker_Rect=screen.blit(colorpicker,(190,225))
    colorfill_Rect= screen.blit(colorfill,(100,225))
    alphaspec_Rect=draw.rect(screen,(255,255,255),(20,570,100,20))
    draw.line(screen,(235,100,5),(40,570),(40,590),3)
    draw.rect(screen,(255,255,0),(20,570,100,20),3)#rect
    square_Rect=screen.blit(square,(10,315))
    line_Rect=screen.blit(line,(100,315))
    circle_Rect=screen.blit(circle,(190,315))
    shapes_Rect=screen.blit(shapes,(10,405))
    text_Rect=screen.blit(text,(100,405))
    select_Rect=screen.blit(select,(190,405))
    marker_Rect=screen.blit(marker,(10,495))
    moreinfo_Rect=screen.blit(moreinfo,(500,650))
    save_Rect=screen.blit(save,(3,3))
    load_Rect=screen.blit(load,(63,3))
    tab_Rect=[]

    
    tab_Rect.append(pencil_Rect)
    tab_Rect.append(eraser_Rect)
    tab_Rect.append(spray_Rect)
    tab_Rect.append(brush_Rect)
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
    tab_Rect.append(colors_Rect)
    tab_Rect.append(Drawcircletool())
    tab_Rect.append(drawsquaretool())
    tab_Rect.append(save_Rect)
    tab_Rect.append(load_Rect)
    for x in range(300,650,75):  #select subs
            draw.rect(screen,(255,255,255),(x,405,50,50))
            draw.rect(screen,(255,255,0),(x,405,50,50),5)
    tab_Rect.append(screen.blit(move,(300,405)))
    tab_Rect.append(screen.blit(resize,(375,405)))
    tab_Rect.append(screen.blit(crop,(450,405)))
    tab_Rect.append(screen.blit(rotate,(525,405)))
    tab_Rect.append(screen.blit(duplicate,(600,405)))
    for x in range(300,650,75):  #select subs
            draw.rect(screen,(255,255,255),(x,315,50,50))
            draw.rect(screen,(255,255,0),(x,315,50,50),5)
    tab_Rect.append(screen.blit(color1,(300,315)))
    tab_Rect.append(screen.blit(color2,(375,315)))
    tab_Rect.append(screen.blit(squarefill,(450,315)))
    tab_Rect.append(screen.blit(squareborder,(525,315)))
    tab_Rect.append(screen.blit(square,(600,315)))
    tab_Rect.append( moreinfo_Rect)
    return(tab_Rect)
screen.blit(helpback,(0,0))
mouse1=0
tabs=[]
toolrects=Drawtools()
while running:
    txtx=345
    txty=55
    mx,my=mouse.get_pos()
    for evt in event.get():
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                mouse1=1
        if evt.type==QUIT:
            running=False
    if mouse1==1:
        for i in range (len(toolrects)):
            if toolrects[-1].collidepoint((mx,my)):
                webbrowser.open("More info.txt")
                break
            elif toolrects[i].collidepoint((mx,my)):
                screen.blit(helpback,(0,0))
                toolrects=Drawtools()
                draw.rect(screen,(255,255,255),(345,55,248,109))
                draw.rect(screen,(230,60,10),toolrects[i],5)
                for k in range(len(discription[i])):
                    sent=myfont.render(discription[i][k],1,(0,0,0))
                    screen.blit(sent,(txtx,txty))
                    txty+=15

    mouse1=0
    display.flip()
quit()

