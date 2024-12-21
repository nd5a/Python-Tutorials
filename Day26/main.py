# # List Comprehension
# # nums = [1, 2, 3]
# # new_list = [n + 1 for n in nums]

# # double = [i*2 for i in range(1,5)]
# # print(double)

# names = ['D', 'Dhruvil', 'asadada', 'eajdk', 'r']
# # short_names = [name for name in names if len(name) < 5]
# # print(short_names)

# title_names = [name.upper() for name in names if len(name) > 5]
# print(title_names)

# # Square of Numbers

# # num = [1,2,3,4,5,6,7,8,9,10]
# # square_num = [i**2 for i in num]
# # print(square_num)


# # problem

# nums_list = [1,1,2,3,5,8,13,21,34,55]
# even_list = [nums for nums in nums_list if nums % 2 == 0]
# print(even_list)

# Dictionary comprehension

# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key, value) in dict.items()}

# import random
# names = ["Alexa", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student : score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# sentence = "What is Your name?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {"Monday" : 12, "Tuesday" : 14, "Wednesday" : 15}

# weather_f = {day : temp*(9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

student_dict = {"student" : ["Dhruvil", "Nakrani", "Arina"], 
                "score": [34,42,92]}

# looping through dictionaries
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)