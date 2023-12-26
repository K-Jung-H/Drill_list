from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('Kirby.png')
Arrow = load_image('hand_arrow.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Aimation(p):
    global direct
    global frame
    global x, y
    x, y = p[0], p[1]

    frame = (frame + 1) % 10
    addition_x, addition_y = 0, 0
    if frame == 0 or frame == 1:
        addition_x = 5
    elif frame == 2 or frame == 3:
        addition_x = 4
    else:
        addition_x, addition_y = 3, 3

    if direct == 'L':
        character.clip_composite_draw(frame * 25 + addition_x, 520, 25, 25 + addition_y,0, 'h', x, y, 100, 100)
    elif direct == 'R':
        character.clip_draw(frame * 25 + addition_x, 520, 25, 25 + addition_y, x, y, 100, 100)

#점을 지정하면 그 위치로 이동하는 경로 만들기 함수
def make_route(p):
    global direct
    x1,y1 = x, y
    x2,y2 = p[0], p[1]

    if x2 > x1:
        direct = 'R'
    else:
        direct = 'L'

    route = []
    for i in range(1, 100, 5):
        t = i / 100
        new_x = (1 - t) * x1 + t * x2
        new_y = (1 - t) * y1 + t * y2
        route.append((new_x, new_y))
    route.append((x2, y2))
    return route

def Arrow_Draw(p):
    mx = p[0]
    my = p[1]
    Arrow.draw(mx,my)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
direct = 'L'


INDEX = 0
points = [random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)]
current_route = make_route(points)

hide_cursor()

while running:

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if INDEX == 19:
        points = (random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT))
        current_route = make_route(points)
    INDEX = (INDEX + 1) % 20

    Aimation(current_route[INDEX])
    Arrow_Draw(current_route[-1])
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()