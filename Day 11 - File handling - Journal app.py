from datetime import datetime

print("----- Journal app ------")

entry = input("Enter your thoughts: ")

with open("D:/Dipen/Python/journal.txt", "a") as file:
    file.write(f"{datetime.now().strftime("%d-%m-%Y")} - {entry}\n")

print("Your entry has been saved!")

with open("D:/Dipen/Python/journal.txt", "r") as file:
    data = file.read()
    print("\n----- All Journal Entries ------")
    print(data)


