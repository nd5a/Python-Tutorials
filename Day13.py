# Debugging

# Describe problem

# def my_fun():
#     for i in range(1,21):
#         if i == 20:
#             print("You Got it")

# my_fun()

# Reproduce the bug

# from random import randint
# dice_img = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_img[dice_num])


# Play Computer

# year = int(input("What's your year of birth ?"))
# if year > 1980 and year < 1994:
#     print("You are millenial")
# elif year >= 1994:
#     print("You are a GEN-Z")

# Fix the Errors

# age = int(input("Enter your Age: "))
# if age > 18:
#     print(f"You can drive at age {age}")

# Print is your best friend

# pages = 0
# words_per_page = 0
# pages = int(input("Number of Pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# # print(pages)
# print(total_words)

# Use a Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13]) 

# search problem and debug it

# number = int(input("Which number do you want to check ? "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# leap year problem 

# year = int(input("Enter Year to check: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Year is leap year")
#         else:
#             print("Not leap")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# Debug fizz buzz excercise

# Fizzbuzz problem

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print([num])