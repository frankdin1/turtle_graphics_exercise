# Methods to import modules
# 1
from turtle import Turtle, Screen
import random

color_array = ['AliceBlue', 'AntiqueWhite', 'AntiqueWhite3', 'AntiqueWhite4', 'aquamarine',
               'aquamarine4', 'azure3', 'azure4', 'beige', 'bisque2', 'bisque4', 'blue', 'blue4',
               'BlueViolet', 'brown', 'brown4', 'burlywood', 'burlywood4']
used_colors = []

direction = ['forward', 'left', 'right', 'backward']
# 2
# import turtle

# 3
# import turtle as t

# 4
# from turtle import *  # not recommended

import heroes

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
print(timmy.shape())


def dash_line(i):
    for _ in range(i):
        timmy.forward(20)
        timmy.pu()
        timmy.forward(10)
        timmy.pd()


def move():
    move_counter = 0
    while move_counter < 11:
        timmy.forward(30)
        timmy.left(90)
        timmy.forward(30)
        timmy.right(90)
        move_counter += 1

move()
def choose_color():
    # choose a random color
    color_choice = color_array[round(random.random() * len(color_array) - 1)]

    # if the random color is already used...
    if color_choice in used_colors:
        while color_choice in used_colors:
            # keep choosing a new color until you find one that has not been used already
            color_choice = color_array[round(random.random() * len(color_array) - 1)]
        # when you find a color that has not been used yet, add it to the array of used colors
        used_colors.append(color_choice)

    # if the random color you picked has not been used yet, add it to the array of used colors
    else:
        used_colors.append(color_choice)
    return used_colors[-1]  # return the last color added to the array of used colors


def descending_staircase(h, ps):
    dash_length = h
    pen_width = ps
    while dash_length >= 1:
        timmy.pensize(pen_width)
        # print two dashed lines
        for _ in range(2):
            dash_line(dash_length)
            timmy.left(90)
        # after every two dashed lines, reduced the length of the dashed lines
        dash_length -= 1

        # reduce the size of the pen but don't go smaller than size  of one
        if pen_width < 1:
            pen_width = 1
        pen_width -= 2
        color = choose_color()
        timmy.pencolor(color)


def draw_shape(number_of_sides):
    while number_of_sides < 11:
        for _ in range(number_of_sides):
            timmy.forward(100)
            timmy.right(360 / number_of_sides)
        number_of_sides += 1
        color = choose_color()
        timmy.pencolor(color)


# initial_number_of_sides = 3
# draw_shape(initial_number_of_sides)

# staircase_height = 10
# pen_size = 20
# descending_staircase(staircase_height, pen_size)

screen.exitonclick()  # this line has to be last
