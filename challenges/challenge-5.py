#draw a spirograph
from turtle import Turtle
import random
import turtle as t

mr_turtle = Turtle()
mr_turtle.shape("turtle")
mr_turtle.speed("fastest")

t.colormode(225)
screen = t.Screen()
screen.colormode(255)
mr_turtle.pencolor(255, 0, 0)

def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    random_color = (r, g, b)
    return random_color


def spirograph( size_of_gap ):
    for i in range(int(360 / size_of_gap)):
        mr_turtle.color(random_color())
        mr_turtle.circle(100)
        mr_turtle.setheading(mr_turtle.heading() + size_of_gap)


spirograph(5)

screen.exitonclick()
