def addition(n1, n2):
    return n1+n2

def Substraction(n1, n2):
    return n1-n2

def Multiplication(n1, n2):
    return n1*n2

def Division(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1/n2

while True:
    print("\n\nBasic calculator:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = input("\nSelect an operation(1-5): ")

    if operation == "5":
        print("It was a good calculator. Thank you!")
        break

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if operation == "1":
        print("Result: ", addition(num1, num2))
    elif operation == "2":
        print("Result: ", Substraction(num1, num2))
    elif operation == "3":
        print("Result: ", Multiplication(num1, num2))
    elif operation == "4":
        print("Result: ", Division(num1, num2))
    else:
        print("Invalid choice. Please select 1-5.") 

