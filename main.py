import pygame as pg
import random
import settings as s
import functions as f

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

pg.time.delay(20)

while True:
    s.FPS.tick(70)

    b = pg.event.get()
    for event in b:
        if event.type == pg.QUIT:
            f.autosave()
            exit()

    f.randomx += 1
    f.randomx2 += 1
    f.randomx3 += 1

    if f.Moving == "r":
        f.x += int(round(f.xVelocity))
    if f.Moving == "l":
        f.x -= int(round(f.xVelocity))
    
    hitbox = pg.Rect(f.x, f.y, 69, 81)
    if hitbox.colliderect(s.girldino.hitbox):
        if f.spoke == False:
            f.blit = True
            f.spoke = True

    f.wait += 1
    if f.wait == 500:
        f.blit = False
        f.spoke = False
        f.wait = 0
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        f.idle = False
        f.xVelocity += 0.5
        if f.xVelocity >= f.MaxSpeed:
           f.xVelocity = f.MaxSpeed
        f.Moving = "r"
        s.player.Idle = s.player.idle2
        f.WalkR()
    elif keys[pg.K_a] or keys[pg.K_LEFT]:
        f.idle = False
        f.xVelocity += 0.5
        if f.xVelocity >= f.MaxSpeed:
           f.xVelocity = f.MaxSpeed
        f.Moving = "l"
        s.player.Idle = s.player.idle1
        f.WalkL()
    else:
        if f.xVelocity > 0:
            f.xVelocity -= 0.2
        f.idle = True
    if f.isjump == False:  
        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            f.jumpcount += 1
            f.isjump = True
    f.Jump()   

    f.EdgeLoop()
    f.Draw()

        
