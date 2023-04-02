#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
from turtle import Turtle, Screen

mr_turtle = Turtle()
mr_turtle.shape("turtle")
    
side = 3
angle = 360 / side 
for i in range(8):

    # this is just to distinguish polygons
    if side % 2 == 0:
        mr_turtle.color("green")
    else:
        mr_turtle.color("red")

    for j in range(side):
        mr_turtle.forward(100)
        mr_turtle.left(angle)

    side += 1
    # this is to get the external angle of the polygons 
    angle = 360/ side

screen = Screen()
screen.exitonclick()
