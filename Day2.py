# Data Types, Numbers, Operations, Type Conversions, f-string

# "String"

# print("Hello"[0:3])

# print("123" + "345")

# # integer
# print(123 + 456)

# # Float

# print(3.143223)

# Boolean True:False

# num = input("Enter Two Digit Number: ")

# Mathematical Operation in Python

# PEMDAS LR (), **, *, /, +, -

# print(2/2*2**2+2-2/(4+5))

# # BMI Calculator
# height = (input("Enter Your Height in m: "))
# weight = (input("Enter Your Weight in kg: "))

# bmi = float(weight) / (float(height)**2)

# print("Your BMI result is: "+str(bmi))

# print(round(8/3,5))

# print( type(8 // 3))

# print(type(4/2))

# score = 1

# # User scores a point
# score += 3
# print(score)

# score = 2
# height = 1.8
# isWinning = True
# print(f"Score is {score}")

# Left Life Days, Weeks and months Calculator

# age = int(input("Enter Your Current Age: "))
# days = age * 365
# weeks = age * 52
# months = age * 12
# print(f"Your age is {days}, {weeks}, {months}")
# live_life = 100

# live_days = (live_life*365)-days
# live_weeks = (live_life*52)-weeks
# live_months = (live_life*12)-months

# print(f"Your Left Life is {live_days}, {live_weeks}, {live_months}")

# Bill Split Calculator

print("Welcome")
bill = float(input("What was the total bill? "))
tip = int(input("How Much tip would you like to give? 10,12 or 15? "))
people = int(input("How Many People to split the bill? "))

tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill+total_tip_amount
bill_per_person = total_bill/people

final_amouont = "{:.2f}".format(bill_per_person,2)
print(f"Each person should pay: {final_amouont}")
