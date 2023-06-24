#
# classes
#

# parent class
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
        
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

# child class, inherit from Vehicle
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

# child class, inherit from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

# instantiation
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
vc1 = Vehicle("black")

print(mc1.wheels)        # 3
print(car1.enginetype)   # gas
print(car2.doors)        # 4
print(vc1.bodystyle)     # black

car1.drive(30)           # Driving my gas car at 30
car2.drive(40)           # Driving my electric car at 40
mc1.drive(50)            # Driving my gas motorcycle at 50
