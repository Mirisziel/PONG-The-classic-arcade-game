from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.write(f"your score: {self.score} ", align="center", font=("courier", 15, "normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Your score: {self.score}", align="center", font=('Arial', 15, 'normal'))

    def end_game(self):
        return True

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("courier", 35, "bold") )