from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.sx = None
        self.sy = None
        self.life = 1

    def draw(self):
        sx = self.sx
        sy = self.sy
        if self.life != 0:
            self.image.draw(sx, sy)
            draw_rectangle(*self.get_bb())

    def update(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        pass

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                self.life = 0
                #game_world.remove_object(self)