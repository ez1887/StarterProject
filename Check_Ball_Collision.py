from Ball import Ball
import numpy as np

#Checks if two balls have collided, if touching return True, else return False
def check_ball_collision(ball_one, ball_two):
    delta_x = ball_one.x - ball_two.x
    delta_y = ball_one.y - ball_two.y
    distance = np.sqrt(delta_x**2 + delta_y**2)
    if distance < ball_one.radius + ball_two.radius:
        return True
    else:
        return False

def update_ball_collision(ball_one, ball_two):
    mass_one = ball_one.density * (4/3) * np.pi * ball_one.radius**3
    mass_two = ball_two.density * (4/3) * np.pi * ball_two.radius**3
