# 이것은 각 상태들을 객체로 구현한 것임.
import random

from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
FLY_SPEED_KMPH = 20.0 # Km / Hour

FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

# x 좌표 시작 지점, y 좌표 시작 지점, 가로 길이, 세로 길이
Bird_Ani = [[0, 330, 190, 176], [190, 330, 190, 176], [380, 330, 175, 176], [555, 330, 175, 176], [730, 330, 190, 176],
            [0, 160, 190, 176], [190, 160, 190, 176], [380, 160, 175, 176], [555, 160, 175, 176], [730, 160, 190, 176],
            [0, 0, 190, 170], [190, 0, 185, 155], [370, 0, 175, 170], [550, 0, 175, 170]]



class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1000), 490
        self.frame = random.randint(0, 14)
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.face_dir * FLY_SPEED_PPS * game_framework.frame_time
        if  self.x >= 1600 -25 or self.x <= 25:
            self.face_dir *= -1
        #self.x = clamp(25, self.x, 1600 - 25)


    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw( Bird_Ani[int(self.frame)][0], Bird_Ani[int(self.frame)][1],  Bird_Ani[int(self.frame)][2],  Bird_Ani[int(self.frame)][3],
                                          0, '', self.x + 25, self.y - 25, 200, 160)
        else:
            self.image.clip_composite_draw(Bird_Ani[int(self.frame)][0], Bird_Ani[int(self.frame)][1],
                                           Bird_Ani[int(self.frame)][2], Bird_Ani[int(self.frame)][3],
                                           0, 'h', self.x + 25, self.y - 25, 200, 160)
