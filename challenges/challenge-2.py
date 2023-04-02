#draw a dotted line
from turtle import Turtle, Screen

mr_turtle = Turtle()
mr_turtle.shape("turtle")
mr_turtle.color("red")

for i in range(20):
    mr_turtle.forward(10)
    mr_turtle.penup()
    mr_turtle.forward(5)
    mr_turtle.pendown()
#     mr_turtle.left(90)


screen = Screen()
screen.exitonclick()
