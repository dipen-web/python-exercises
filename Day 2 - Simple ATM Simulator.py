# 💡 Project: Simple ATM Simulator
# A basic command-line ATM that lets the user:

# Check balance
# Deposit money
# Withdraw money
# Exit

# ✅ Features:
# Start with ₹1000 in the account.

# Show a menu with options:
# 1: Check balance
# 2: Deposit
# 3: Withdraw
# 4: Exit

# Loop continues until user selects Exit.

# Prevent withdrawal if balance is low.

# Ignore negative deposit or withdrawal.

balance = 1000 # store starting amount

while True:
    print("Welcome! What would you like to do?")
    print("1: Check balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Exit")
    
    choice = input("Choose an option(1-4): ")

    if choice == "1":
        print(f"Your current balance is {balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Please enter a valid amount.")
            continue
        else:
            balance += amount
            print(f"{amount} deposited successfully.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Please enter a valid amount.")
            continue
        elif balance - amount <= 0:
            print("Not enough money to withdraw.")
            continue
        else:
            print(f"{amount} withdrew successfully.")
            balance -= amount
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Try again!")



