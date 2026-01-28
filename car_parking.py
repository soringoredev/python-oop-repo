class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
            print(f"The {self.color} {self.brand} is starting!")


car1 = Car('Toyota', 'red')
car2 = Car('Honda','blue')
car3 = Car('Ford','green')

print(car3.color)  # green

parking_lot = [car1, car2, car3]

for car in parking_lot:
    car.start_engine()