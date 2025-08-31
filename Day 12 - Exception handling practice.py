# try:
#     num = int(input("Enter a number: "))
#     print(num / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Please enter a valid number.")

try:
    file = open("data.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
finally:
    print("Done with file operation.")
