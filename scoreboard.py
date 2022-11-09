from turtle import Turtle
from snake import Snake
from food import Food

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
            self.clear()
            self.score += 1
            self.goto(0, 0)
            self.write(f"Game over", True, align="center", font=('Arial', 12, 'normal'))

    def score_counter(self):
            self.clear()
            self.score += 1
            self.goto(0, 280)
            self.write(f"Score: {self.score}", True, align="center", font=('Arial', 12, 'normal'))
