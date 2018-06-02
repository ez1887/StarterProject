def position_change(ball, time_step):
    ball.x = ball.x + ball.vx * time_step
    ball.y = ball.y + ball.vy * time_step