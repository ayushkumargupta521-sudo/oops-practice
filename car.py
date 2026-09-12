class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def fullname(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petro or Diesel"


class ElectricCar(Car):

    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "S", "80Kh")
print(my_car.fuel_type())

car = ElectricCar("Tesla", "M", "90")

my_car = Car("Rollce Royce", "BM")
print(my_car.fuel_type())

print(Car.total_car)