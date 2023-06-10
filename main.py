class Car:
    def __init__(self, WheelNumber, PSI, FuelType ):
        self.WheelNumber = WheelNumber
        self.PSI = PSI
        self.FuelType = FuelType

        def get_WheelNumber(self):
            return self.WheelNumber

        def get_PSI(self):
            return self.PSI

        def get_FuelType(self):
            return self.FuelType

    def show(self):
        print(self.WheelNumber, self.PSI, self.FuelType)

    def honk(self):
            print("Wallah im Honking")

    def drive(self):
            print("Wallah im driving")

car = Car("4", "30", "Diesel")
car.show()
car.drive()

car2 = Car("4", "20", "Benzin")
car2.show()
car2.honk()

car3 = Car("2", "25", "Soler")
car3.show()
car.drive()
car.honk()