from enum import Enum
class Vehicle:
    class FuelType(Enum):
        DIESEL = 'Diesel'
        PATROL = 'Patrol'
        GASOLINE = 'Gasoline'

    def check_psi(self, psi: float):
        if psi > self.max_psi:
            raise ValueError ("PSI is Higher than the allowed maximum amount")


    def __init__(self, speed_of_vehicle=50, max_speed_of_vehicle=100, psi=25, max_psi=40, number_of_wheels=4, fuel_type=FuelType.GASOLINE):
        self.speed_of_vehicle = speed_of_vehicle
        self.max_speed_of_vehicle = max_speed_of_vehicle
        self.psi = psi
        self.max_psi = max_psi
        self.check_psi(psi)
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type


# Drive Function:
    def drive(self, speed_of_vehicle: int):
        if speed_of_vehicle > self.max_speed_of_vehicle:
            raise ValueError("Current speed is above the maximum possible speed")
        self.speed_of_vehicle = speed_of_vehicle
        print("Walla Vehicle is driving at " + str(speed_of_vehicle) + " KMH")


    def increase_speed_of_vehicle(self, amount_of_speed_increase: int):
        self.amount_of_speed_increase = amount_of_speed_increase
        self.speed_of_vehicle += self.amount_of_speed_increase
        print(f"Vehicle is now driving in  {self.speed_of_vehicle}  KMH")


    def decrease_speed_of_vehicle(self, amount_of_speed_decrease: int):
        self.amount_of_speed_decrease = amount_of_speed_decrease
        self.speed_of_vehicle -= amount_of_speed_decrease
        print(f"Vehicle is now driving in  {self.speed_of_vehicle} KMH")
        if self.speed_of_vehicle < 0:
            raise ValueError("You cannot drive below 0 KMH")


#Pump Tires Function:
    def pump_tires(self, amount_of_psi_to_pump: float):
        print("Filling air in the tires....")
        self.amount_of_psi_to_pump = amount_of_psi_to_pump
        if self.psi + amount_of_psi_to_pump > self.max_psi:
            raise ValueError ("Amount of PSI pumped is higher than allowed maximum")
        print("Tires have completed filling up. PSI: ", self.psi + self.amount_of_psi_to_pump)





