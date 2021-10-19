from turtle import Turtle, Screen
import random
colors = ["red", "green", "purple", "orange", "blue", "yellow", "brown", "black"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def create_turtle():
    t = Turtle()
    t.shape("turtle")
    return t


def create_racers():
    racer_list = []
    for i in range(0,7):
        t = create_turtle()
        t.color(colors[i])
        racer_list.append(t)
    return racer_list


def position_racers(racers):
    ypos = -150
    for racer in racers:
        racer.penup()
        racer.goto(x=-230,y=ypos)
        ypos += 50


def start_race(racers):
    winner = False
    while not winner:
        for racer in racers:

            racer.forward(random.randint(1, 10))
            xpos = racer.xcor()
            if xpos > 210:
                winner = True
                winning_color = racer.color()
                if winning_color[0] == user_bet:
                    print(f"You win! {winning_color[0]} won the race!")
                else:
                    print(f"You lose! {winning_color[0]} won the race!")






racers = create_racers()
position_racers(racers)
start_race(racers)


screen.exitonclick()
