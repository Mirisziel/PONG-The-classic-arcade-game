from turtle import Turtle
coordinates = [(-350,0), (350,0)]
UP = 90
DOWN = 270
class Paddle:
    def __init__(self):
        self.paddles = []
        self.creation()


    def creation(self):
        for loc in coordinates:
            self.paddle = Turtle(shape="square")
            self.paddle.color("white")
            self.paddle.shapesize(stretch_wid=1, stretch_len=5)
            self.paddle.penup()
            self.paddle.goto(loc)
            self.paddle.setheading(90)
            self.paddles.append(self.paddle)
    def move(self):
        pass
        self.paddles[0].forward(10)
        self.paddles[1].forward(10)
    def left_up(self):
        self.paddles[0].setheading(UP)
        self.paddles[0].forward(10)
    def left_down(self):
        self.paddles[0].setheading(DOWN)
        self.paddles[0].forward(10)

    def right_up(self):
        self.paddles[1].setheading(UP)
        self.paddles[1].forward(10)
    def right_down(self):
        self.paddles[1].setheading(DOWN)
        self.paddles[1].forward(10)

    def left(self):
        return self.paddles[0]

    def right(self):
        return self.paddles[1]

class Center:
    def __init__(self):
        self.create()
        
    def create(self):
        self.new = Turtle()
        self.new.color("white")
        self.new.hideturtle()
        self.new.penup()
        self.new.goto(0, 300)
        self.new.setheading(270)
        for _ in range(30):
            self.new.penup()
            self.new.forward(20)
            self.new.pendown()
            self.new.forward(20)
        