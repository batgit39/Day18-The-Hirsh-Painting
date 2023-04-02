import random
# from turtle import Screen
import turtle as t

mr_turtle = t.Turtle()
mr_turtle.hideturtle()
t.colormode(225)

screen = t.Screen()
screen.colormode(255)
mr_turtle.pencolor(255, 0, 0)

mr_turtle.speed("fastest")
mr_turtle.pensize(20)
angle = [90,180,270,360]


def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    random_color = (r, g, b)
    return random_color


for i in range(200):
    mr_turtle.color(random_color())
    mr_turtle.forward(50)

    if i % 2 == 0:
        mr_turtle.right(random.choice(angle))
    else:
        mr_turtle.left(random.choice(angle))


mr_turtle.pencolor(random_color())
screen.exitonclick()
