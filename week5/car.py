class Car:
    def __init__(self, make, model, year) :
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
            print(f"make: {self.make}")
            print(f"model: {self.model}")
            print(f"year: {self.year}")
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kwh")
    
my_car = Car("Tesla", "camry", 2008)
my_car.display_info()
my_electric_car = ElectricCar("Tesla", "camry", 2008, 100)
my_electric_car.display_info()