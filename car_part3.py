 car_part3.py
class Car:
    def __init__(self, brand, model, year, wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.wheels = wheels
        self.speed = 0

    def drive(self):
        if self.wheels >= 4:
            print(f"{self.brand} {self.model} is now driving!")
        else:
            print(f"{self.brand} {self.model} cannot drive – not enough wheels!")

    def accelerate(self):
        self.speed += 10
        print(f"Current Speed: {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} {self.model} stopped! Speed = {self.speed} km/h")

my_car = Car("Toyota", "Vios", 2024, 4)
my_car.drive()
my_car.accelerate()
my_car.accelerate()
my_car.stop()
