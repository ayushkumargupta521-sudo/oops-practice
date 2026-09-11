class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery


my_car = ElectricCar("Tesla","S","80Kh")
print(my_car.fullname())


# my_car = Car("Rollce Royce","BM")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())