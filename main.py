import pygame as pg
import random
import settings as s

try:
    from saves import x
except ImportError:
    print('var not found')
    x = s.player.x
try:
    from saves import y
except ImportError:
    y = s.player.y
    print('var not found')

pg.init()

idle = True
frame = 1
xVelocity = 0
MaxSpeed = 5
Moving = ""
jumpcount = 0
count = 0
jumpforce = 10
gravity = 1
isjump = False


randomx = random.randrange(50, 750)
randomy = random.randrange(50, 250)

randomx2 = random.randrange(50, 750)
randomy2 = random.randrange(50, 250)

randomx3 = random.randrange(50, 750)
randomy3 = random.randrange(50, 250)

pg.time.delay(20)

def refresh():
    s.pg.display.update()

def TotalRefresh():
    s.pg.display.update()
    s.display.fill((255,255,255))
def LoadClouds():
    global randomx, randomy
    global randomx2, randomy2
    global randomx3, randomy3
    s.display.blit(s.background.cloud2, (randomx, randomy))
    s.display.blit(s.background.cloud2, (randomx2, randomy2))
    s.display.blit(s.background.cloud2, (randomx3, randomy3))
    if randomx == 870:
        randomx = -150
        randomy = random.randrange(50, 250)
    if randomx2 == 870:
        randomx2 = -150
        randomy2 = random.randrange(50, 250)
    if randomx3 == 870:
        randomx3 = -150
        randomy3 = random.randrange(50, 250)
def LoadGround():
    s.display.blit(s.background.ground, (0, 180))
    s.display.blit(s.background.ground, (300, 180))
    s.display.blit(s.background.ground, (600, 180))
def LoadPlayer():
    global y, x
    if idle == True:
        s.display.blit(s.player.Idle,(x,y))

def EdgeLoop():
    global y, x
    if x >= 880:
       x = -80 
    if x <= -90:
        x = 870
        
def Draw():
    LoadClouds()
    LoadPlayer()
    LoadGround()
    TotalRefresh()

def WalkR():
    global y, x
    global frame
    if frame < 1.9:
        frame += 0.1
    else:
        frame = 0
    s.display.blit(s.player.animation[int(frame)], (x,y))
def WalkL():
    global y, x
    global frame
    if frame < 1.9:
        frame += 0.1
    else:
        frame = 0
    s.display.blit(s.player.animation2[int(frame)], (x,y))
def autosave():
    global y, x
    save = open("saves.py", "w")
    text_list = ["x = "+str(x)+"\n", "y = "+str(y)+"\n"]
    save.writelines(text_list)
    save.close()


while True:
    s.FPS.tick(70)

    b = pg.event.get()
    for event in b:
        if event.type == pg.QUIT:
            autosave()
            exit()

    randomx += 1
    randomx2 += 1
    randomx3 += 1

    if Moving == "r":
        x += int(round(xVelocity))
    if Moving == "l":
        x -= int(round(xVelocity))
    
    keys = pg.key.get_pressed()

    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        idle = False
        xVelocity += 0.5
        if xVelocity >= MaxSpeed:
           xVelocity = MaxSpeed
        Moving = "r"
        s.player.Idle = s.player.idle2
        WalkR()
    elif keys[pg.K_a] or keys[pg.K_LEFT]:
        idle = False
        xVelocity += 0.5
        if xVelocity >= MaxSpeed:
           xVelocity = MaxSpeed
        Moving = "l"
        s.player.Idle = s.player.idle1
        WalkL()
    else:
        if xVelocity > 0:
            xVelocity -= 0.2
        idle = True
    if isjump == False:  
        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            jumpcount += 1
            isjump = True

    if isjump :
        if jumpforce > 0:
            y -= int(jumpforce)
            jumpforce -= 0.5
        if jumpforce == 0:
            y += int(gravity)
            gravity += 0.5
            if y >= 370:
                y = 370
                gravity = 1
                jumpforce = 10
                isjump = False
        

    EdgeLoop()
    Draw()

        
