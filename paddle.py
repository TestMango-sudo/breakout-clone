from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_right(self):
        right_x = self.xcor() + 20
        self.goto(right_x, self.ycor())

    def move_left(self):
        left_x = self.xcor() - 20
        self.goto(left_x, self.ycor())
