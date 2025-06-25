#------- Import Section -------------
from turtle import Turtle


class Scoreboard(Turtle):
    font_size = 20

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()
        self.game_over = False

    def update_scoreboard(self):
        x, x2, x3 = -360, -100, 240
        y = 270
        align = "left"
        self.clear()
        self.goto(x, y)
        self.write(f"Score: {self.score}", align=align, font=("arial", self.font_size, "bold"))
        self.goto(x2, y)
        self.color("Blue")
        self.write("Break Out Clone", align=align, font=("arial", self.font_size, "bold"))
        self.goto(x3, y)
        self.color("white")
        self.write(f"Lives: {self.lives}", font=("arial", self.font_size, "bold"))
        self.color("red")
        self.goto(350, 270)
        self.write("♥️", font=("arial", 25, "bold"))
        self.color("white")

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()
        if self.lives == 0:
            game_over = True

    def gain_life(self):
        self.lives += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.update_scoreboard()


class ScreenTop(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.width(5)
        self.goto(-400, 270)
        self.setheading(360)
        self.pendown()
        self.forward(800)
