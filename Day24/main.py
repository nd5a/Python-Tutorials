# file = open('E:\Python Tutorials\Day24\my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# Read File
# with open('E:\Python Tutorials\Day24\my_file.txt') as file:
#     contents = file.read()
#     print(contents)
    
# # Write File
# with open('E:\Python Tutorials\Day24\my_file.txt', mode="a") as file:
#     file.write("\n New Text")
    
# Create New File
# with open('E:\Python Tutorials\Day24\ew_file.txt', mode="w") as file:
#     file.write("My Name is ")

with open("E:\Python Tutorials\Day24\Good Snake Game\data.txt") as f:
    print(f.read())