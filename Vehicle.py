from enum import Enum
class Vehicle:
    class FuelType(Enum):
        DIESEL = 'Diesel'
        PATROL = 'Patrol'
        GASOLINE = 'Gasoline'

    def check_psi(self, psi: float):
        if psi > self.max_psi:
            raise ValueError ("PSI is Higher than the allowed maximum amount")


    def __init__(self, speed_of_vehicle, max_speed_of_vehicle, psi, max_psi, number_of_wheels, fuel_type):
        self.speed_of_vehicle = speed_of_vehicle
        self.max_speed_of_vehicle = max_speed_of_vehicle
        self.psi = psi
        self.max_psi = max_psi
        self.check_psi(psi)
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type

    def drive(self, speed_of_vehicle: int):
        print("Walla Vehicle is driving at " + str(speed_of_vehicle) + " KMH")
    def fill_up_tires(self, psi: float):
        print("Filling air in the tires....")
        self.psi = psi
        print("Tires have completed filling up. PSI: ", self.psi)


car1 = Vehicle(50, 60, 30, 45, 3, Vehicle.FuelType.GASOLINE)
psi_value = car1.psi
wheels_value = car1.number_of_wheels

car1.drive(50)

print("PSI", psi_value)
print("Number of wheels", wheels_value)
print("Fuel Type", Vehicle.FuelType)




