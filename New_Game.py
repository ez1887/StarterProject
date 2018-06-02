#Main code for game/simulation

import numpy as np
from Ball import Ball

numBalls = int(input('Enter the number of balls: '))
wall_x_low = 0
wall_x_high = 1
wall_y_low = 0
wall_y_high = 1
max_vel = 1

#Create all Ball objects with random positions and velocities
ball_list = []
for i in range(numBalls):
    ball_list.append(Ball(np.random.uniform(wall_x_low, wall_x_high), np.random.uniform(wall_y_low, wall_y_high), np.random.uniform(0, max_vel), np.random.uniform(0, max_vel)))