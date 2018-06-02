from Ball import Ball
import numpy as np 

def check_wall_collision(ball, wallpos):
# ball is object of Ball class
# wallpos is list of 4 numbers in order [left x, right x, bottom y, top y]

    if ((ball.x - ball.radius) < wallpos[0]):
        return 0
    elif ((ball.x + ball.radius) > wallpos[1]):
        return 1
    elif ((ball.y - ball.radius) < wallpos[2]):
        return 2
    elif ((ball.y + ball.radius) > wallpos[3]):
        return 3
    else:
        return -1

def update_wall_collision(ball, wallnum):
#collision occurs with left wall if 0, right wall if 1, bottom wall if 2, top wall if 3
    if (wallnum == 0 or wallnum == 1):
        ball.vx = -ball.vx
    elif (wallnum == 2 or wallnum == 3):
        ball.vy = -ball.vy
    return [ball.vx, ball.vy]