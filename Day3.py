# Conditional Statements , Logical Operators, Code Blocks and Scope

# print("Welcome to the RollerCoaster !")
# height = int(input("What is your height in cm?"))

# if height>120:
#     print("You can Ride RollerCoaster")
# else:
#     print("Sorry, You can't Ride RollerCoaster")

# num = int(input("Enter Number to Chcek whether it is even or odd? "))

# if num%2==0:
#     print(f"{num} is Even Number")
# else:
#     print(f"{num} is Odd Number")

# Nested Statements :

# height = int(input("Enter Your Height in cm: "))
# if height>120:
#     print("you can ride")
#     age = int(input("Enter Your age: "))
#     if age<=18:
#         print("You can ride for 7$")
#     else:
#         print("You can ride for 12$")
# else:
#     print("Sorry, You can't ride")

# height = int(input("Enter Your Height in cm: "))
# if height>120:
#     print("you can ride")
#     age = int(input("Enter Your age: "))
#     if age<12:
#         print("You can ride for 7$")
#     elif age<=18:
#         print("You can ride for 12$")
#     else:
#         print("You can ride for 15$")
# else:
#     print("Sorry, You can't ride")

# MBI 2.0 Calculator

# height = float(input("Enter your height in (m): "))
# weight = int(input("Enter Your Weight in Kg: "))
# bmi = round(weight/(height**2)) 

# if bmi>18.5:
#     if bmi<25:
#         print(f"Your BMI is {bmi}, You are Normal")
#     elif bmi<30:
#         print(f"Your BMI is {bmi},You are Overweight") 
#     elif bmi<35:
#         print(f"Your BMI is {bmi},You are Obese")
#     else:
#         print(f"Your BMI is {bmi},You are Clinically Obese")
# else:
#     print(f"Your BMI is {bmi},You are Underweight")

# Leap year Check:

# year = int(input("Enter Year to check: "))

# if  year%4==0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else: 
#     print("Not a Leap Year")

height = int(input("Enter Your Height in cm: "))
bill = 0

if height >=120:
    print("You can Ride RollerCoaster")
    age = int(input("Enter Your Age: "))
    if age<12:
        bill=5
        print("Child Tickets are 5$")
    elif age<=18:
        bill=7
        print("Youth Tickets are 7$")
    else:
        bill=12
        print("Adult Tickets are 12$")
    wants_photo = input("Do you want to take Photo? Y or N: ")
    if wants_photo == "Y":
        bill+=3
    print(f"Your Final Bill is : {bill}")
else:
    print("Sorry You can't Ride")
