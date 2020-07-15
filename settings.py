import pygame as pg

pg.init()

FPS = pg.time.Clock()

display = pg.display.set_mode((800, 500)) #Make a window that is 800 by 500 px
display.fill((255,255,255))
pg.display.set_caption("The Amazing Dino") #Set the caption of the window

class player(): #Make the player class
    x = 400
    y = 370 #Set the x and y varibles

    width = 69
    height = 81 #The width and height of the player/character

    centerx = x + round(width / 2)
    centery = y + round(height / 2) #the center position variables of the player

    frame1 = pg.image.load("Dino/Dino-running-1.png") 
    frame2 = pg.image.load("Dino/Dino-running-2.png")
    frame3 = pg.image.load("Dino/Dino-running-3.png") 
    frame4 = pg.image.load("Dino/Dino-running-4.png") #loading the frames for player animation

    idle1 = pg.image.load("Dino/Dino-idle-1.png")
    idle2 = pg.image.load("Dino/Dino-idle-2.png")

    Idle = idle2
    
    animation = [frame1, frame2]
    animation2 = [frame3, frame4]
player = player()

class background():
    cloud = pg.image.load("tiles/cloud.png") #load a image of a cloud
    cloud2 = pg.image.load("tiles/BackCloud.png") #load a image of a lighter cloud
    ground = pg.image.load("tiles/ground.png")
background = background()
