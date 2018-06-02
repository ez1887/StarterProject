#Main code for game/simulation

import numpy as np
import matplotlib.pyplot as plt
import time
from Ball import Ball
from Check_Ball_Collision import check_ball_collision
from Check_Ball_Collision import update_ball_collision
from Check_Wall_Collision import check_wall_collision
from Check_Wall_Collision import update_wall_collision
from Position_Change import position_change

#get input variables
numBalls = int(input('Enter the number of balls: '))
wall_x_low = 0
wall_x_high = 1
wall_y_low = 0
wall_y_high = 1
wallpos = [wall_x_low, wall_x_high, wall_y_low, wall_y_high]
max_vel = 0.5
t_run = 5
t_step = 0.01   

#Create all Ball objects with random positions and velocities
ball_list = []
for i in range(numBalls):
    ball_list.append(Ball(np.random.uniform(wall_x_low, wall_x_high), np.random.uniform(wall_y_low, wall_y_high), np.random.uniform(-max_vel, max_vel), np.random.uniform(-max_vel, max_vel)))
    print(ball_list[i].x)
    print(ball_list[i].y)


#Iterate through time


for t in range(0, int(t_run/t_step)):
    x1 = []
    y1 = []
    for i in range(numBalls):
        wall_collision_num = check_wall_collision(ball_list[i], wallpos)
        if (wall_collision_num >= 0):
            [ball_list[i].vx, ball_list[i].vy] =  update_wall_collision(ball_list[i], wall_collision_num)
        for j in range(i+1, numBalls):
            ball_collision_tf = check_ball_collision(ball_list[i], ball_list[j])
            if (ball_collision_tf):
                [ball_list[i].vx, ball_list[i].vy, ball_list[j].vx, ball_list[j].vy] = update_ball_collision(ball_list[i], ball_list[j])
    for i in range(numBalls):
        [ball_list[i].x, ball_list[i].y] = position_change(ball_list[i], t_step)
        x1.append(ball_list[i].x)
        y1.append(ball_list[i].y)
    print("x = " + str(ball_list[0].x) + " y = " + str(ball_list[0].y) + " vx = " + str(ball_list[0].vx) + " vy = " + str(ball_list[0].vy))
    plt.scatter(x1, y1, s=50, marker="o")
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.show(block=False)
    plt.pause(t_step)
    # time.sleep(t_step)
    plt.close()
# plt.plot(x2, y2)
# plt.plot(x3, y3)
