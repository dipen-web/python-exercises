# Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         print(self.name, "is walking.")

# class Student(Person): #student inherits from person
#     def study(self):
#         print(self.name, "is studying.")

# s1 = Student("Rahul")
# # s1 has attribute - name
# # s1 has methods - walk and study
# s1.study()
# s1.walk()

# # print programmer defined attributes associated with an object
# print(f"\n{s1.__dict__}")

# # Get all attributes and methods of an object including buil-in
# print(f"\n{dir(s1)}")

# Encapsulation

class BankAccount:
    def __init__(self, balance): # a bank account will have balance, so property can be balance
        self.__balance = balance # hidden(private) - you should not be able to directly change your account balance as you like.

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance. Please enter proper number.")
        else:
            self.__balance = self.__balance - amount
            print(f"Amount {amount} withdrawn successfully.")
    
    def get_balance(self):
        print(f"Your current balance is {self.__balance}")

acc1 = BankAccount(25000)
print(acc1.__balance)

acc1.deposit(10000)
acc1.get_balance()

acc1.withdraw(15000)
acc1.get_balance()
        
