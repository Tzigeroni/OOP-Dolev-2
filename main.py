class Car:
    def __customize__(self, number_of_wheels: int, psi: float, fuel_type: str):
        self.number_of_wheels = number_of_wheels
        self.psi = psi
        self.fuel_type = fuel_type

        def get_number_of_wheels(self):
            return self.number_of_wheels

        def get_psi(self):
            return self.psi

        def get_fuel_type(self):
            return self.fuel_type

    def show(self):
        print(self.number_of_wheels, self.psi, self.fuel_type)

    def honk(self):
            print("Wallah im Honking")

    def drive(self):
            print("Wallah im driving")

car = Car(4, 30, "Diesel")
car.show()
car.drive()

car2 = Car(4, 20, "Benzin")
car2.show()
car2.honk()

car3 = Car(2, 25, "Soler")
car3.show()
car.drive()
car.honk()