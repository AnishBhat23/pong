from turtle import *
from paddle import Paddle
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle1 = Paddle(-380)
screen.onkey(fun=paddle1.go_up, key="w")
screen.onkey(fun=paddle1.go_down, key="s")

paddle2 = Paddle(370)
screen.onkey(fun=paddle2.go_up, key="Up")
screen.onkey(fun=paddle2.go_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()