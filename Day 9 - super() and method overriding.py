class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        # self.name = name
        # self.age = age
        # Instead of writing above code, you can use super() and call parent's constructor which has the same code you wanted.
        super().__init__(name, age)
        self.grade = grade

s1 = Student("Manoj", 16, "A")
print("Name -", s1.name)
print("Age -", s1.age)
print("Grade -", s1.grade)

# Anothe example with methods

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound() # call parent's method
        print("Dog barks") # if we remove the super() line and keep the other code same, then it will be method overiding.

d = Dog() # creating object
d.sound() # calling that object's method
        