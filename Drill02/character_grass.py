from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x1 = 0
x2 = 800
while (x1 < 800):
    clear_canvas_now() #게임 렌더링 부분
    grass.draw_now(400,30) #게임 렌더링 부분
    character.draw_now(x1,90) #게임 렌더링 부분
    character.draw_now(x2,90) #게임 렌더링 부분
    
    x1 = x1+2 #게임 로직 부분
    x2 = x2 - 2 #게임 로직 부분
    delay(0.01)

close_canvas()
