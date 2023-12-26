from pico2d import *
import math

def move(direct):
    global x1,y1
    if  direct == 1:
            x1 = x1+2
    elif    direct == 2:
            y1 = y1 + 2
    elif direct == 3:
            x1 = x1 - 2
    elif    direct == 4:
            y1 = y1 - 2

def turn():
    global x1,y1,direct
    if x1 == 780 and y1 ==90:
            direct = 2
    elif x1 ==780 and y1 == 600:
            direct = 3
    elif x1 == 0 and y1 == 600:
            direct = 4
    elif x1 == 0 and y1 == 90:
            direct = 1

open_canvas()
grass = load_image('grass.png')
character = load_image('D:character.png')
global direct

x1 = 400
y1 = 90
direct = 1
angle = 271

RECT = True


while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x1,y1)
    if RECT == True:
        turn()
        move(direct)
        if  x1 == 400 and y1 == 90:
            RECT = False
            
    else:    
        x1 = math.cos(math.radians(angle))*255 + 400
        y1 =  math.sin(math.radians(angle))*255 + 300
        angle +=1
        angle%=360
        if  angle == 270:
            angle = 271
            x1 =400
            y1 = 90
            RECT = True
    
    delay(0.01)








close_canvas()
