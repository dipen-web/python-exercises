# import 

# f = open("D:\Dipen\Python\Day 11 - File handling.txt", "w")
# # data = f.readline()

# # print(data) # string

# # with open("D:\Dipen\Python\Day 11 - File handling.txt") as f:
# #     data = f.read()
# #     print(data)

# f.write("Now the file has more content.")
# f.close()

# f = open("D:\Dipen\Python\Day 11 - File handling.txt", "r")
# data = f.read()
# print(data)


# reading a file
# we are opening the file for the purpose of reading and with "with" keyword we are closing the file automatically.
# with open("D:/Dipen/Python/Day 11 - File handling.txt", "r") as file:
#     data = file.read()
#     print(data)

# writing in a file = "w" is written for that purpose
with open("D:/Dipen/Python/Day 11 - File handling.txt", "w") as file:
    file.write("My first line\n")
    file.write("My second line and its big.")

with open("D:/Dipen/Python/Day 11 - File handling.txt", "r") as file:
    data = file.read()
    print(data)