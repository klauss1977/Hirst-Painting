from turtle import Turtle, Screen
# import colorgram
# #from image import image.jpg
# colors = colorgram.extract("image.jpg", 22)
#
#
# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
import random

color_list = [(236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94),
              (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79),
              (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35),
              (239, 161, 192), (148, 25, 24)]

turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()


def draw_circle():
    fill_color = random.choice(color_list)
    tim.fillcolor(fill_color)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()


def draw_10_circles():
    for _ in range(10):
        draw_circle()
        tim.penup()
        tim.forward(30)
        tim.pendown()


def move_to_start_line(coord_y):
    tim.penup()
    tim.goto(0, coord_y)
    tim.pendown()


for lines in range(1, 11):
    y_coord = lines * 30
    draw_10_circles()
    move_to_start_line(y_coord)

screen = Screen()
screen.exitonclick()
