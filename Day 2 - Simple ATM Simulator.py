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
    print("\nWelcome! What would you like to do?")
    print("1: Check balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Exit")
    
    choice = input("\nChoose an option(1-4): ")

    if choice == "1":
        print(f"\nYour current balance is {balance:.2f}")
    elif choice == "2":
        amount = float(input("\nEnter amount to deposit: "))
        if amount <= 0:
            print("\nPlease enter a valid amount.")
            continue
        else:
            balance += amount
            print(f"\n{amount:.2f} deposited successfully.")
            print(f"Your new balance is {balance:.2f}")
    elif choice == "3":
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("\nPlease enter a valid amount.")
            continue
        elif balance - amount < 0:
            print("\nNot enough money to withdraw.")
            continue
        else:
            balance -= amount
            print(f"\n{amount:.2f} withdrew successfully.")
            print(f"\nYour new balance is {balance:.2f}")
    elif choice == "4":
        print("\nThank you for using the ATM.\n")
        break
    else:
        print("\nInvalid option. Try again!")



