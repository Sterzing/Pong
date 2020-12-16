from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.coord = coord
        self.screen = Screen()
        self.shape("square")
        self.penup()
        self.goto(coord)
        self.shapesize(5, 1)

    def right_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def right_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def left_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


