# # More Turtle Graphics

# from turtle import Turtle, Screen

# new_turtle = Turtle()
# screen = Screen()

# def move_forwards():
#     new_turtle.forward(10)

# def move_backwards():
#     new_turtle.backward(10)

# def turn_left():
#     new_heding = new_turtle.heading() + 10
#     new_turtle.setheading(new_heding)

# def turn_right():
#     new_heding = new_turtle.heading() - 10
#     new_turtle.setheading(new_heding)

# def clear():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.exitonclick()

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# User bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Validate user input
if user_bet in colors:
    is_race_on = True
else:
    print("Invalid color entered. Please restart and enter a valid color.")
    screen.exitonclick()

# Turtle race
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break 

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
