# with open("E:\Python Tutorials\Day25\weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("E:\Python Tutorials\Day25\weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row[1])
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

# import pandas

# data = pandas.read_csv("E:\Python Tutorials\Day25\weather-data.csv")
# print(data["temp"])


import pandas

data = pandas.read_csv("")