from turtle import Turtle, Screen
import tkinter as tk
import time
import winsound
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard, ScreenTop
from bricks import Brick
from open import OpenMessage, GameOverMessage


game_live = False
game_over = False
brick_colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan"]
brick_hits = {"red": 1, "orange": 2, "yellow": 3, "green": 2, "blue": 3, "purple": 2, "cyan": 3}
brick_distance = 60
x1 = -370 + 25
y1 = 190 + brick_distance
bricks = []


#Create a Turtle graphics screen
screen = Screen()
screen.bgcolor("black")
screen.title("Break Out Clone")
screen.setup(width=800, height=600)
screen.tracer(0)


def draw_bricks():
    for j in range(len(brick_colors)):
        y_val = y1 - j * 25
        for i in range(9):
            x_val = x1 + i * (brick_distance + 25)
            b = Brick(x_val, y_val, brick_colors[j])
            bricks.append(b)


def do_stuff():
    global game_live, game_over
    game_live = True
    ball = Ball((0, -242))
    pad = Paddle((0, -260))
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(pad.move_left, "Left")
    screen.onkeypress(pad.move_right, "Right")
    pad.move_left()
    pad.move_right()
    draw_bricks()

    OM.clear()
    button.destroy()
    tb = ScreenTop()
    winsound.Beep(300, 5)
    while game_live:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move_ball()

        # detect wall collision
        if ball.ycor() > 265:
            winsound.Beep(300, 5)
            ball.bounce_y()
        if ball.ycor() < -280:
            winsound.Beep(600, 5)
            scoreboard.lose_life()
            if scoreboard.lives == 0:
                game_over = True
            ball.goto(0, -242)
            pad.goto(0, -260)
            ball.move_ball()
        if ball.xcor() > 380 or ball.xcor() < -380:
            winsound.Beep(300, 5)
            ball.bounce_x()
        # detect collision with paddle
        if ball.distance(pad) < 60 and ball.ycor() < - 260:
            winsound.Beep(300, 5)
            ball.bounce_y()
        for Brick in bricks:
            if ball.distance(Brick) < 30:
                ball.bounce_x()
                Brick.delete()
                x_axis_difference = ball.distance(Brick)
                y_axis_difference = ball.distance(Brick)
                if x_axis_difference > y_axis_difference:
                    # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                    ball.bounce_x()
                else:
                    # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                    ball.bounce_x()
                    ball.bounce_y()
                scoreboard.score += 1
                scoreboard.update_scoreboard()
        if game_over:
            ball.clear()
            pad.clear()
            GameOverMessage()
            screen.exitonclick()


if __name__ == "__main__":
    canvas = screen.getcanvas()
    scoreboard = Scoreboard()
    OM = OpenMessage()
    button = tk.Button(canvas.master, text="START!", command=do_stuff, bg="lightblue")
    canvas.create_window(-8, 100, window=button)


# Keep the screen open until manually closed
screen.mainloop()
