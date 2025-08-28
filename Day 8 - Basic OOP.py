class Car:
        
    # define init constructor
    # car will have some data about it / properties
    def __init__(self, brand, model, top_speed):
        self.brand = brand
        self.model = model
        self.top_speed = top_speed
        self.is_running = False

    def print_details(self):
        print("Car Details:")
        print(f"Brand - {self.brand}\nModel - {self.model}\nTop speed - {self.top_speed}")

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("The car is running!")
        else:
            print("The car is alredy running.")

    def stop(self):
        if self.is_running:
            print("The car has been stopped.")
            self.is_running = False
        else:
            print("The car has been already stopped.")


# create object1 for BMW car
car1 = Car("Audi", "Q6", 240)

# You need to actually start the car and stop the car. Consider it a real-life scenario.
car1.print_details()
# print the details about the car

# start the car
car1.start()
# stop the car
car1.stop()

car1.stop()
car1.start()
    

