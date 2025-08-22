# Write a Python program that lets a user manage a grocery list.
# The program should allow the user to:

# 1. View the grocery list
# 2. Add an item
# 3. Remove an item
# 4. Search for an item
# 5. Sort the list
# 6. Exit the program

grocery_list = []

while True:
    print("\nGrocert list manager:\n")
    print("1. View the grocery list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Search for an item")
    print("5. Sort the list")
    print("6. Exit the program")

    choice = input("\nSelect the choice(1-6): ")

    if choice == "1":
        # view the items
        if len(grocery_list) == 0:
            print("No items added yet in the Grocery List.")
        else:
            print(", ".join(grocery_list))
    elif choice == "2":
        # add an item
        grocery_item = input("Enter item name: ")
        grocery_list.append(grocery_item)
        print("Item added successfully.")
    elif choice == "3":
        # remove the item
        item = input("\nEnter the item to be removed:")
        grocery_list = [i for i in grocery_list if i.lower()!= item.lower()]
        
        if len(grocery_list) == 0:
            print("Grocery list is empty now.")
        else:
            print(f"New grocery list after removing {item}")
            print(", ".join(grocery_list))
    elif choice == "4":
        # search the item
        item = input("Enter item to search: ").lower()

        if item in [i.lower() for i in grocery_list]:
            print(f"{item} is in the list.")
        else:
            print(f"{item} is not in the list.")
    elif choice == "5":
        # sort the list
        grocery_list.sort()
        print(", ".join(grocery_list))
    elif choice == "6":
        print("\nThank you for using our program.\n")
        break
    else:
        print("Please select correct choice.")



