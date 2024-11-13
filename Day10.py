# Functions with Outputs

# def my_fun():
#     result = 3*2
#     return result
# print(my_fun())

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "Please Provide Valid Inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your First Name: "),input("What is your Last Name: ")))

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     if month > 12 or month <1:
#         return "Invalid Month"
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_leap(year) and month == 2:
#         return 29   
#     return month_days[month - 1]
        

# year = int(input("Enter a Year: "))
# month = int(input("Enter a Month: "))
# days = days_in_month(year, month)
# print(days)

# DOC Strings


# def format_name(f_name, l_name):
#     """Take a first name and last name to format it"""
#     if f_name == "" or l_name == "":
#         return "Please Provide Valid Inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your First Name: "),input("What is your Last Name: ")))


# Calculator
import os

def clear():
    # Clear the console for cross-platform use
    os.system('cls' if os.name == 'nt' else 'clear')

print('''
 _____________________
|  _________________  |
| | DN-Python    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|                                         
                                     ''')   

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero is not allowed"
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Enter an operation from the line above: ")
        if operation_symbol not in operations:
            print("Invalid operation. Please choose a valid operation.")
            continue

        num2 = float(input("Enter the second number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        user_choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'e' to exit: ").lower()
        if user_choice == "y":
            num1 = answer
        elif user_choice == "e":
            should_continue = False
        else:
            should_continue = False
            clear()
            calculator()

calculator()
