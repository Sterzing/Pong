from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "yellow"
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pong")
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.right_up, "Up")
screen.onkeypress(right_paddle.right_down, "Down")
screen.onkeypress(left_paddle.left_up, "w")
screen.onkeypress(left_paddle.left_down, "s")
speed = 0.1
game_running = True
while game_running:
    screen.update()
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 \
            or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        speed -= 0.01

    if ball.xcor() > 400:
        ball.reset()
        speed = 0.1
        scoreboard.update_l_score()

    if ball.xcor() < -400:
        ball.reset()
        speed = 0.1
        scoreboard.update_r_score()

screen.exitonclick()
