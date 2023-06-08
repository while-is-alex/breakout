from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from walls import Walls
from blocks import Blocks
from playsound import playsound

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=800)
screen.title("Breakout")
screen.tracer(0)

# Objects
ball = Ball()
paddle = Paddle((0, -360))
scoreboard = Scoreboard()
walls = Walls()
blocks = Blocks()

# Inputs
screen.listen()
screen.onkey(paddle.left, 'Left')
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'a')
screen.onkey(paddle.right, 'd')
screen.onkey(ball.tilt_table, 't')
screen.onkey(ball.start_moving, 'space')


# Game
is_on = True
ball.set()
while is_on:
    screen.update()
    # Checks if the user has pressed the input to start the game
    if ball.running:
        ball.move()
        scoreboard.remove_instructions()

    # Increases the ball speed
    if ball.move_speed == 4:
        if 50 <= scoreboard.current_score:
            ball.move_speed += 1
    if ball.move_speed == 5:
        if 250 < scoreboard.current_score:
            ball.move_speed += 1
            paddle.move_speed += 5
    if ball.move_speed == 6:
        if 1000 < scoreboard.current_score:
            ball.move_speed += 1
            paddle.move_speed += 5
    if ball.move_speed == 7:
        if 5000 < scoreboard.current_score:
            ball.move_speed += 1
            paddle.move_speed += 10

    # Detects collision with the wall
    if ball.xcor() > 220:
        # Checks if the ball is going in the right direction
        # to avoid multiple bounces
        if ball.heading() < 90 or ball.heading() > 270:
            ball.bounce_x()
            playsound('game_sounds/wall.m4a')
    if ball.xcor() < -230:
        if ball.heading() > 90 or 270 > ball.heading():
            ball.bounce_x()
            playsound('game_sounds/wall.m4a')
    # Detects collision with the ceiling
    if ball.ycor() > 275:
        ball.bounce_y()
        playsound('game_sounds/wall.m4a')

    # Detects collision with the paddle and which part of the paddle it is touching
    for paddle_part in paddle.paddle:
        if ball.distance(paddle_part) < 30 and ball.ycor() < -340:
            # Checks if the ball is going in the right direction (downwards)
            # before bouncing it, making sure it doesn't bounce repeatedly
            if ball.heading() > 180:
                part = paddle.paddle.index(paddle_part) + 1
                ball.bounce_y(part=part)
                playsound('game_sounds/paddle.m4a')

    # Detects collision with a block
    for block in blocks.green_blocks:
        if ball.distance(block) < 30:
            ball.block_bounce(screen)
            blocks.destroy_green_block(block)
            scoreboard.point(5)
            playsound('game_sounds/block.m4a')

    for block in blocks.yellow_blocks:
        if ball.distance(block) < 30:
            ball.block_bounce(screen)
            blocks.destroy_yellow_block(block)
            scoreboard.point(10)
            playsound('game_sounds/block.m4a')

    for block in blocks.orange_blocks:
        if ball.distance(block) < 30:
            ball.block_bounce(screen)
            blocks.destroy_orange_block(block)
            scoreboard.point(25)
            playsound('game_sounds/block.m4a')

    for block in blocks.red_blocks:
        if ball.distance(block) < 30:
            ball.block_bounce(screen)
            blocks.destroy_red_block(block)
            scoreboard.point(50)
            playsound('game_sounds/block.m4a')

    # Detects when the level has been cleared
    if blocks.clear_level_check():
        scoreboard.lives += 3
        ball.ball_reset()

    # Detects when paddle misses
    if ball.ycor() < -390:
        ball.ball_reset()
        scoreboard.lose_life()
        if scoreboard.lives < 1:
            scoreboard.game_over = True
            scoreboard.check_high_score()
            is_on = False

    # Detect when TILT is caused
    if ball.tilt > 4:
        scoreboard.tilt = True
        playsound('game_sounds/tilt.wav')
        scoreboard.check_high_score()
        is_on = False

# Screen remains open until it's clicked
screen.exitonclick()
