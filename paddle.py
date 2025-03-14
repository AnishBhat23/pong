from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=xcor,y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:
            self.goto(self.xcor(), new_y)
