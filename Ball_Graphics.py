#Main code for simulation - adding better ball graphics in - ONLY CHANGE SECTION AT BOTTOM WHERE GRAPHICS ARE DONE

#imports
import numpy as np
import matplotlib.pyplot as plt
import time
from Ball import Ball
from Check_Ball_Collision import check_ball_collision
from Check_Ball_Collision import update_ball_collision
from Check_Wall_Collision import check_wall_collision
from Check_Wall_Collision import update_wall_collision
from Position_Change import position_change
from turtle import *

#get input variables
numBalls = int(input('Enter the number of balls: '))
wall_x_low = 0
wall_x_high = 1
wall_y_low = 0
wall_y_high = 1
wallpos = [wall_x_low, wall_x_high, wall_y_low, wall_y_high]
max_vel = 0.5
t_run = 10
t_step = 0.01   

#Create all Ball objects with random positions and velocities
ball_list = []
for i in range(numBalls):
    ball_list.append(Ball(np.random.uniform(wall_x_low, wall_x_high), np.random.uniform(wall_y_low, wall_y_high), np.random.uniform(-max_vel, max_vel), np.random.uniform(-max_vel, max_vel)))
    print(ball_list[i].x)
    print(ball_list[i].y)

#Iterate through time
for t in range(0, int(t_run/t_step)):
    x = []
    y = []
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
        x.append(ball_list[i].x)
        y.append(ball_list[i].y)
    print("x = " + str(ball_list[0].x) + " y = " + str(ball_list[0].y) + " vx = " + str(ball_list[0].vx) + " vy = " + str(ball_list[0].vy))
    
    ## THIS IS THE SECTION TO CHANGE - GETTING X AND Y WORKS YAY 
    #plt.scatter(x, y, marker="o")
    #plt.ylim(0, 1)
    #plt.xlim(0, 1)
    #plt.show(block=False)
    #plt.pause(t_step)
    # time.sleep(t_step)
    #plt.close()
    
    for i in range(numBalls):
        turtle.setposition(x[i], y[i])
        turtle.circle(ball_list[i].radius)
    turtle.delay(t_step*1000)            #time delay in miliseconds
    turtle.clear()                       #should clear screen

