from enum import Enum
from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, speed_of_vehicle=100, max_speed=150, psi=30, max_psi=50, number_of_wheels=4, fuel_type=Vehicle.FuelType.GASOLINE, number_of_doors=5):
        super().__init__(speed_of_vehicle, max_speed, psi, max_psi, number_of_wheels, fuel_type)
        self.number_of_doors = number_of_doors



