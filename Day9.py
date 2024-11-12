# Dictionaries and Nesting

# format of Dictionarie:
# key : value

# {
#     "Bug": "An error in a program
#     "Code": "The part of a program that a computer can execute",
#     "loop":"A sequence of instructions that a computer can execute repeatedly",
#     "function":"A block of code that can be used repeatedly in a program",
# }

programming_dictionary = {"Bug": "An error in a program",

    "function":"A block of code that can be used repeatedly in a program",}

# print(programming_dictionary["function"])

# # Adding new items to dictionary
# programming_dictionary["loop"] = "A sequence of instructions that a computer can execute repeatedly"
# print(programming_dictionary)

# # Create an empty dictionary
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
# programming_dictionary["Bug"] = " A Bug"
# print(programming_dictionary)

# Loop through a dictionary

# for keys in programming_dictionary:
#     print(keys) # prints keys
#     print(programming_dictionary[keys])

# Grading Program Exercise

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# students_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         students_grades[student] = "Outstanding"
#     elif score > 80:
#         students_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         students_grades[student] = "Acceptable"
#     else:
#         students_grades[student] = "Fail"

# print(students_grades)


# Nesting 

# {
#     key : [List],
#     key2 : {Dict}
# }

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Norway": "Oslo",
# }

# # Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lyon"],
#     "Germany" : ["Berlin", "Munich"],
# }

# # Nesting Dictionary in dictionary

# travel_log = {
#     "France": {"cities_visited" : ["Paris", "Lyon"], "total_visited": 12},
#     "Germany" : ["Berlin", "Munich"],
# }

# # Nesting Dictionary in List

# travel_log = [
#    {"country" :  "France", 
#     "cities_visited" : ["Paris", "Lyon"], 
#     "total_visited": 12
#     },
   
#    {"country": "Germany" , 
#     "cities_visited" : ["Berlin", "Munich"],  
#     "total_visited": 5
#     }
# ]
# print(travel_log)

# travel_log = [
#    {"country" :  "France", 
#     "visits" : 12,
#     "cities" : ["Paris", "Lyon"], 
#     },
   
#    {"country": "Germany" , 
#     "visits": 5,
#     "cities" : ["Berlin", "Munich"],  
#     }
# ]

# def add_new_country(country_visited, time_visited, cities_visited):
#     new_country = {
#         "country": country_visited,
#         "visits": time_visited,
#         "cities": cities_visited
#         }
#     travel_log.append(new_country)
#     print(travel_log)
# add_new_country("India", 5, ["Delhi", "Mumbai"])

# Blind Auction 

from replit import clear

print(  '''  ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\ ''')
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} won with bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is Your Name? : ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are they any other bidders? Type 'yes' or 'no': ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()