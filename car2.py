# car_part2.py
class Car:
    def __init__(self, brand, model, year, wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.wheels = wheels

car1 = Car("Toyota", "Vios", 2024, 4)
car2 = Car("Honda", "Civic", 2023, 4)
car3 = Car("Ford", "Ranger", 2022, 4)
car4 = Car("Mitsubishi", "L300", 2021, 4)

print(f"Car 1: {car1.brand} {car1.model}, Year: {car1.year}, Wheels: {car1.wheels}")
print(f"Car 2: {car2.brand} {car2.model}, Year: {car2.year}, Wheels: {car2.wheels}")
print(f"Car 3: {car3.brand} {car3.model}, Year: {car3.year}, Wheels: {car3.wheels}")
print(f"Car 4: {car4.brand} {car4.model}, Year: {car4.year}, Wheels: {car4.wheels}")
