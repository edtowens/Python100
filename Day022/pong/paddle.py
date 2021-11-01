from turtle import Turtle
MOVE_DISTANCE = 30
PLAYER1_POSITION = (350, 0)
PLAYER2_POSITION = (-350, 0)


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.player_position(player)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def player_position(self, player_num):
        if player_num == 1:
            self.goto(PLAYER1_POSITION)
        else:
            self.goto(PLAYER2_POSITION)
