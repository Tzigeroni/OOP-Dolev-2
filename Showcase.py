from Vehicle import Vehicle
from Car import Car


vehicle1 = Vehicle()
vehicle2 = Vehicle()
car3 = Car()


vehicle1.drive(50)
vehicle1.increase_speed_of_vehicle(50)
vehicle1.decrease_speed_of_vehicle(40)


car3 = Car(100,200,40,60,4,Vehicle.FuelType.PATROL,4)
car3.increase_speed_of_vehicle(50)
car3.pump_tires(20)