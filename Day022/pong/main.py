from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ed's Pong Game")
screen.tracer(0)
player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.08)
    screen.update()
    ball.move()

    # Check collision with ceiling and floor heading in the east direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball went off the screen
    if ball.xcor() > 380:
        # player2 scores a point, reset ball and send towards player 2
        scoreboard.increment_l_score()
        ball.reset_position()
    elif ball.xcor() < -380:
        # player1 scores a point, reset ball and send towards player 1
        scoreboard.increment_r_score()
        ball.reset_position()




screen.exitonclick()
