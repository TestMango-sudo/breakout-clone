from turtle import Turtle


class Brick(Turtle):
    def __init__(self, pos_x, pos_y, col):
        super().__init__()
        self.shape("square")
        self.color(col)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(pos_x, pos_y)

    def delete(self):
        self.goto(-350, -450)

