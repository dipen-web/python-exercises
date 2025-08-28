# Step 1: Understand the requirement
# Step 2: Decide properties (attributes)
# Step 3: Decide actions (methods)
# Step 4: Plan inheritance
# Step 5: Write it step by step

# parent class / base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}.")

# child class
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        print(f"Employee ID - {self.employee_id}\nSalary - {self.salary}")

# Create a Person
p1 = Person("Dipen", 30)
p1.introduce()

# Create an Employee
e1 = Employee("Dipen", 30, "005", 50000)
e1.introduce()
e1.show_details()