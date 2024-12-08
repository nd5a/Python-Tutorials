# # from turtle import Turtle, Screen

# # tim = Turtle()
# # # timmy_the_turtle.shape("")

# # for _ in range(4):
# #     tim.forward(50)
# #     tim.right(90)



# # screen = Screen()
# # screen.exitonclick()

# # import turtle
# # tim = turtle.Turtle()

# # from turtle import Turtle
# # tim = Turtle()

# # from turtle import *

# # import turtle as t
# # tim = t.Turtle()

# import turtle as t

# tim = t.Turtle()

# # for _ in range(20):
# #     tim.forward(5)
# #     tim.pd()
# #     tim.forward(5)
# #     tim.pu()


# import random
# # colors = ["red", "yellow", "blue", "green", "IndianRed", "wheat"]

# # def draw_shape(num_sides):
# #     angle = 360 / num_sides
# #     for _ in range(num_sides):
# #         tim.forward(100)
# #         tim.right(angle)

# # for shape_side_n in range(3,11):
# #     tim.color(random.choice(colors))
# #     draw_shape(shape_side_n)

# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# import turtle as t

# import random
# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
    
#     random_color = (r, g, b)
    
#     return random_color

# tim.speed("fastest")

# def draw_spirograph(size_of_gap):
    
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         # current_heading = tim.heading()
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(1)
# tim.circle(100)
# screen = t.Screen()
# screen.exitonclick()

import colorgram

# rgb_colors = []

# colors = colorgram.extract('img.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)    


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(23, 37, 49), (62, 22, 42), (37, 92, 127), (151, 22, 72), (7, 7, 7), (152, 51, 97), (27, 38, 33), (21, 78, 97), (217, 57, 105), (44, 50, 113)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.seth(225)
tim.fd(300)
tim.seth(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.seth(90)
        tim.fd(50)
        tim.seth(180)
        tim.fd(500)
        tim.seth(0)

screen = turtle_module.Screen()
screen.exitonclick()