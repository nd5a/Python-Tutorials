# OOPs Concept 
# Object Oriented Programming

# import another_module 
# print(another_module.another_variable)
# import turtle

# #  object.method
# # timmy = turtle.Turtle()

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(20)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
print(table)

print(table.align)