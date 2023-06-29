from Vehicle import Vehicle
from Car import Car

print("Welcome to the test drive ")

car = Car()
vehicle = Vehicle()


while True:
    choice = input("Would you like to start driving? -- Please choose Y / N?: ").upper()
    if choice == "N":
        print("Exiting test drive")
        break

    while True:
        speed = int(input("\nEnter the speed of the vehicle: "))
        speed = car.speed_of_vehicle
        if speed > car.max_speed:
            print("Current speed is above the allowed maximum speed, please choose again. ")
        else:
            break
    while True:
        psi = float(input("\nEnter the PSI of the vehicle: "))
        psi = car.psi
        if psi > car.max_psi:
            print("PSI is higher than allowed maximum, please choose again")
        else:
            break

    while True:
        num_doors = int(input("\nEnter number of doors (2 or 4): "))
        if num_doors != 2 and num_doors != 4:
            print("Invalid number of doors, please ener either 2 or 4. ")
        else:
            break

    while True:
        fuel_input = input("\nEnter the fuel type of the vehicle (Diesel/Patrol/Gasoline): ")
        try:
            fuel_type = Vehicle.FuelType[fuel_input.upper()]
            break
        except KeyError:
            valid_fuel_types = ", ".join(member.name for member in Vehicle.FuelType)
            print(f"Invalid fuel type, Please enter one of the following options: {valid_fuel_types}")


    print(f"\nYou are now driving at {speed} KMH, Your car's PSI is {psi}. \nYour car has {num_doors} doors and is using {fuel_input} as fuel \n")

    while True:

        print("\nPlease choose what action you would like to do : ")
        print("1. Increase speed.")
        print("2. Decrease speed.")
        print("3. Fill up tires.")
        print("4. Exit test drive.")



        action_choice = input("\nPlease choose (1 - 4): ")
        if action_choice == "4":
            print("Exiting test drive")

        if action_choice == "1":
            while True:
                 increase_speed = int(input("\nPlease Choose by how many KMH you would like to increase speed: "))
                 if speed + increase_speed > car.max_speed:
                    print("Current speed increase plus current speed is above the possible maximum, please choose again")
                 else:
                    car.increase_speed_of_vehicle(increase_speed)
                    break



        elif action_choice == "2":
            while True:
                decrease_speed = int(input("\nPlease Choose by how many KMH you would like to decrease speed: "))
                if speed - decrease_speed < 0:
                    print("Current speed minus decreased speed cannot be below zero, please choose again")
                else:
                    car.decrease_speed_of_vehicle(decrease_speed)
                    break


        elif action_choice == "3":
            while True:
                pump_psi = int(input("\nPlease choose how much PSI you would like to pump to the tires"))
                if pump_psi + psi > car.max_psi:
                    print("Current PSI + Pump PSI is exceeds the maximum PSI, please choose again")
                else:
                    car.pump_tires(pump_psi)
                    break


        else:
            print("\nPlease choose a valid action")





















