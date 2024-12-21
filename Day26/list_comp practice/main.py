with open(r"E:\Python Tutorials\Day26\list_comp practice\text1.txt") as file1:
    file1_data = file1.readlines()
with open(r"E:\Python Tutorials\Day26\list_comp practice\text2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)