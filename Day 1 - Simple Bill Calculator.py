# 🧠 Exercise: Simple Bill Calculator

# 🎯 What this program will do:

# Ask the user for the name of an item
# Ask for the price of one item
# Ask for the quantity purchased
# Calculate the total bill
# Show a thank you message with the total

item_name = input("Enter name of the item: ")
item_price = float(input("Enter price of the item: "))
item_quantity = int(input("Enter quantity: "))

total_bill = item_price * item_quantity

print(f"You bought {item_quantity} {item_name} for {total_bill} rs.")
print("Thank you for your purchase.")