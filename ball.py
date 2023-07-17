from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.06

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_cor *= -1

    def collide(self):
        self.x_cor *= -1
        self.move_speed *= 0.9
    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.06
