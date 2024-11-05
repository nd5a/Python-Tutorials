# # Randomisation and Python Lists

# import random

# # random_integer = random.randint(0,100000)
# # print(random_integer)

# # random_float = random.random()*5
# # print(random_float)

# # Head or Tail

# # random_side = random.randint(0,1)
# # if random_side == 1:
# #     print("Head")
# # else:
# #     print("Tail")
    
# # Lists

# # states_of_india = ["Gujarat", "Rajashthan", "Kerala", "Maharashtra"]
# # # print(states_of_india)
# # # states_of_india[1] = "Panjab"
# # # states_of_india.append("Delhi")
# # states_of_india.extend(["New York", "Alaska"])
# # print(states_of_india)


# # Split string method

# name_string  = input("Enter Name with sepatated with comma: ")
# names = name_string.split(", ")

# # # num_items = len(names)
# # # random_choice = random.randint(0,num_items-1)
# # # person_who_will_pay = names[random_choice]

# # person_who_will_pay = random.choice(names)
# # print(person_who_will_pay + " is going to buy the meal today.")

# # num_items = len(names)

# # random_choice = random.randint(0, num_items-1)
# # person_who_will_pay = names[random_choice]
# # print(person_who_will_pay + " is going to buy the meal today.")


# states_of_india = ["Gujarat", "Rajashthan", "Kerala", "Maharashtra"]
# print(states_of_india[3])

# fruits = ["Strawberiies",
#           "Bananas", "Apples", "Mangoes",
#           "Pineapples", "Watermelon", "Grapes"]
# vegetables = ["Spinach", "Kale", "Tomatoes",
#               "Cucumber", "Carrots", "Broccoli", "Peas"]
# dirty_dozon = [fruits, vegetables]
# print(dirty_dozon)

# Treasure 

# row1 = ["📦", "📦", "📦"]
# row2 = ["📦", "📦", "📦"]
# row3 = ["📦", "📦", "📦"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position  = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# # selected_row = map[vertical-1]
# # selected_row[horizontal-1] = "X "

# map[vertical-1][horizontal-1] = "X "

# print(f"{row1}\n{row2}\n{row3}")

# Rock, Paper, Scissors Game

import random
user_input = int(input("Enter Your Choice from : (Type 0 for Rock, Type 1 for scissors, type 2 for paper) :"))

computer_choice = random.choice([0,1,2])
print("Computer Chooses: ",computer_choice)

if user_input == computer_choice : 
    print("It's a tie!")
elif user_input != computer_choice :
    if user_input == 0:
        if computer_choice == 1:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    if user_input == 1:
        if computer_choice == 0:
            print("Scissors cuts rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    if user_input == 2:
        if computer_choice == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
else:
    print("Invalid Input")