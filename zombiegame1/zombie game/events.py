from pygame import*
screen=display.set_mode((1000,650))
screen.fill((0,0,0))

while True:
    print(event.get())
    for evt in event.get():
        if evt.type==MOUSEBUTTONDOWN and reloaddelay==50:
             running=0
