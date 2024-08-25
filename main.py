import random
import turtle
from turtle import Turtle , Screen
turtle.colormode(255)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
mbappe = Turtle()
mbappe.speed(0)
mbappe.hideturtle()
mbappe.penup()
mbappe.setheading(225)
mbappe.forward(300)
mbappe.setheading(0)
number_of_dots = 100
for dot in range(1,number_of_dots+1):
    mbappe.dot(20,random.choice(color_list))
    mbappe.forward(50)
    if dot % 10 == 0:
        mbappe.setheading(90)
        mbappe.forward(50)
        mbappe.setheading(180)
        mbappe.forward(500)
        mbappe.setheading(0)
screen = Screen()
screen.exitonclick()
