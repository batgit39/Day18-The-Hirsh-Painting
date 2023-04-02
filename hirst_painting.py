# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# # print(colors[0])
# for color in colors:
    # r = color.rgb.r
    # g = color.rgb.g
    # b = color.rgb.b
    # new_colors = (r,g,b)
    # rgb_colors.append(new_colors)

# print(rgb_colors)
#using the above code we get the data for colors variable(listed below)


colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
(170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
(145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
(183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
(12, 70, 64), (107, 127, 153),(176, 192, 208), (168, 99, 102)]

import random
import turtle as t


mr_turtle = t.Turtle()
t.colormode(225)

screen = t.Screen()
screen.colormode(255)
mr_turtle.pencolor(255, 0, 0)
mr_turtle.penup()
mr_turtle.hideturtle()

mr_turtle.speed("fastest")


x = -275
y = -225
for i in range(10):
    mr_turtle.setpos(x,y)
    for j in range(10):
        mr_turtle.forward(50)
        mr_turtle.dot(30,random.choice(colors))
    y += 50


# print(mr_turtle.pos())

screen.exitonclick()
