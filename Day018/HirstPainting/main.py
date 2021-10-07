###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as t
t.colormode(255)
tim = t.Turtle()
# tim.pensize()
tim.shape("circle")
tim.home()
tim.penup()
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
for i in range(1, 11):
    for _ in range(10):
        tim.showturtle()
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.fd(50)
    tim.hideturtle()
    tim.sety(i * 50)
    tim.setx(0)

tim.hideturtle()
tim.home()









screen = t.Screen()
screen.exitonclick()