from pico2d import *


open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1000,800
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Kirby.png')

def handle_events():
    global running
    global direct

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                direct = 'L'
            elif event.key == SDLK_RIGHT:
                direct = 'R'
            elif event.key == SDLK_UP:
                direct = 'U'
            elif event.key == SDLK_DOWN:
                direct = 'D'
        elif event.type == SDL_KEYUP:
                direct = 'STOP'


def ANIMATION():
    global frame
    global s_counter
    global x, y
    if direct == 'L':
        character.clip_composite_draw(8 + frame * 23, 570, 23, 23, 0, 'h', x, y, 200, 200)
        frame = (frame + 1) % 9
        x -= 10

    elif direct == 'R':
        character.clip_draw(8 + frame * 23, 570, 23, 23, x, y, 200, 200)
        frame = (frame + 1) % 9
        x += 10

    elif direct == 'U':
        frame = (frame + 1) % 5
        if frame < 3:
            c_size = 23 + frame * 2
        else:
            c_size = 23 + 2 * (6 // frame)

        additional_length = sum(i for i in range(1, frame))
        character.clip_draw(8 + frame * 23 + additional_length, 490, c_size, c_size, x, y, 200, 200)
        y += (frame-1) * 10

    elif direct == 'D':
        frame = (frame + 1) % 10
        addition_x, addition_y = 0, 0
        if frame == 0 or frame == 1:
            addition_x = 5
        elif frame == 2 or frame == 3:
            addition_x = 4
        else:
            addition_x,addition_y = 3, 3
        character.clip_draw(frame * 25 + addition_x, 520, 25, 25 + addition_y, x, y, 200, 200)
        y -= frame * 3

    elif direct == 'STOP':
        character.clip_draw(8 + s_counter * 23, 620, 23, 23, x, y, 200, 200)
        frame = (frame + 1) % 20
        s_counter = frame // 10

def Check_Range():
    global direct
    if (y + 50) >= TUK_HEIGHT and direct == 'U':
        direct = 'STOP'
    elif (y - 30) <= 0 and direct == 'D':
        direct = 'STOP'
    elif (x - 30) <= 0 and direct == 'L':
        direct = 'STOP'
    elif (x + 30) >= TUK_WIDTH and direct == 'R':
        direct = 'STOP'


running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
s_counter = 0
frame = 0
direct = 'STOP'

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    ANIMATION()
    update_canvas()
    handle_events()
    Check_Range()
    delay(0.05)

close_canvas()
