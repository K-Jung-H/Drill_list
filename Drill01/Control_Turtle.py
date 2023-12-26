import turtle as T



def move(direct):
    if direct == 'w':
        T.setheading(90)
    elif direct == 'a':
        T.setheading(180)
    elif direct == 's':
        T.setheading(270)
    elif direct == 'd':
        T.setheading(0)

    T.stamp()
    T.forward(50)

def move_w():
    move('w')

def move_a():
    move('a')

def move_s():
    move('s')

def move_d():
    move('d')


def restart():
    T.reset()


T.shape('turtle')

T.onkey(move_w, 'w')
T.onkey(move_a, 'a')
T.onkey(move_s, 's')
T.onkey(move_d, 'd')
T.onkey(restart,'Escape')
T.listen()
