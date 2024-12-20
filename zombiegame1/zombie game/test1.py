from pygame import*
screen=display.set_mode((1000,650))
player=image.load("character/playerpistol.png")

crop_surf = transform.chop(player,(10,10,20,20))

screen.blit(crop_surf,(0,0))

display.flip()
