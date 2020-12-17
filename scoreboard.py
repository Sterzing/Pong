from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.post_scores()

    def post_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("Arial", 40, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.post_scores()

    def update_r_score(self):
        self.r_score += 1
        self.post_scores()

