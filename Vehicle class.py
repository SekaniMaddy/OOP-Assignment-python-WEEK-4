# Vehicle class
class Vehicle:
    def move(self):
        pass

# Inherited classes: Car, Plane, Boat
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Use polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()