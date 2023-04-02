#draw a square
from turtle import Turtle, Screen

mr_turtle = Turtle()
mr_turtle.shape("turtle")
mr_turtle.color("red")

for i in range(4):
    mr_turtle.forward(100)
    mr_turtle.left(90)


screen = Screen()
screen.exitonclick()
