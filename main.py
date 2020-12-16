from turtle import Screen
from paddle import Paddle
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

screen.listen()
screen.onkeypress(right_paddle.right_up, "Up")
screen.onkeypress(right_paddle.right_down, "Down")
screen.onkeypress(left_paddle.left_up, "w")
screen.onkeypress(left_paddle.left_down, "s")

game_running = True
while game_running:
    screen.update()

screen.exitonclick()
