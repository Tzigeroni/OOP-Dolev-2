from enum import Enum
from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, speed_of_vehicle, max_speed_of_vehicle, psi, max_psi, number_of_wheels, fuel_type, number_of_doors):
        super().__init__(speed_of_vehicle, max_speed_of_vehicle, psi, max_psi, number_of_wheels, fuel_type)
        self.number_of_doors = number_of_doors



# need to inherit from Vehicle
#need to add number of doors option

car1 = Car(0, 100, 40, 50, 4, Vehicle.FuelType.GASOLINE, 5)

print("PSI", car1.psi)
print("Number of wheels", car1.number_of_wheels)
print("Fuel Type", car1.fuel_type.value)
print("number of doors",  car1.number_of_doors)

