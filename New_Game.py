#Main code for game/simulation

import numpy as np
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
max_vel = 1
t_run = 10
t_step = 1   

#Create all Ball objects with random positions and velocities
ball_list = []
for i in range(numBalls):
    ball_list.append(Ball(np.random.uniform(wall_x_low, wall_x_high), np.random.uniform(wall_y_low, wall_y_high), np.random.uniform(0, max_vel), np.random.uniform(0, max_vel)))

print(ball_list[0].vx)
print(ball_list[0].vy)


#Iterate through time
for t in range(0, t_run, t_step):
    for i in range(numBalls):
        wall_collision_num = check_wall_collision(ball_list[i], wallpos)
        if (wall_collision_num>0):
            [ball_list[i].vx, ball_list[i].vy] =  update_wall_collision(ball_list[i], wall_collision_num)
        for j in range(i+1, numBalls):
            ball_collision_tf = check_ball_collision(ball_list[i], ball_list[j])
            if (ball_collision_tf):
                [ball_list[i].vx, ball_list[i].vy, ball_list[j].vx, ball_list[j].vy] = update_ball_collision(ball_list[i], ball_list[j])
    for i in range(numBalls):
        [ball_list[i].x, ball_list[i].y] = position_change(ball_list[i], t_step)
    print(ball_list[0].x) 
    print(ball_list[0].y)