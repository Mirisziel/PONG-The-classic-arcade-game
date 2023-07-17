from turtle import Screen
from Paddle import Paddle,Center
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
paddle = Paddle()
ball = Ball()
center = Center()
score_left = ScoreBoard((-200, 270))
score_right = ScoreBoard((200, 270))
screen.listen()
screen.onkey( paddle.left_up, "w")
screen.onkey( paddle.left_down, "s")
screen.onkey( paddle.right_up, "Up")
screen.onkey( paddle.right_down, "Down")
screen.onkey(score_right.end_game, "Escape")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    screen.listen()
    paddle.move()
    ball.move()

    # Detecting collision with walls
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce()
    # Detecting collision with paddles
    if ball.distance(paddle.right()) < 50 and ball.xcor() > 320 or ball.distance(paddle.left()) < 50 and ball.xcor() < -320:
        ball.collide()

    # Detecting ball ot of bound from right
    if ball.xcor() > 420:
        ball.restart()
        ball.collide()
        score_left.score_increase()
    # Detecting ball out of bound from left
    if ball.xcor() < -420:
        ball.restart()
        ball.collide()
        score_right.score_increase()


screen.exitonclick()
