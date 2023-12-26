from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self): # 클래스 이름은 대문자로 시작하느 명사..
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 500), random.randint(90, 500)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



class Ball21:
    def __init__(self):
        self.x, self.y = random.randint(0,800), random.randint(700, 800)
        self.image = load_image('ball21x21.png')
        self.life = 1

    def update(self):
        if self.life == 1:
            self.y -= 5
            if self.y <= 60:
                self.life = 0

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)


class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(0,800), random.randint(700, 800)
        self.image = load_image('ball41x41.png')
        self.life = 1

    def update(self):
        if self.life == 1:
            self.y -= 8
            if self.y <= 60:
                self.life = 0

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)



def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls21
    global balls41
    global world

    running = True
    world = []

    grass = Grass() # 클래스를 이용해 객체를 찍어냄.
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team

    balls21 = [Ball21() for i in range(11)]
    world += balls21

    balls41 = [Ball41() for i in range(11)]
    world += balls41


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
        o.draw()
    update_canvas()



open_canvas()
# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
