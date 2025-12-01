class Car:
    def __init__(self, make, model, year, rate):
        self.make = make
        self.model = model
        self.year = year
        self.rate = rate
        self.isRented = False

    def is_available(self):
        return not self.isRented

    def set_rented(self, days):
        self.isRented = True
        print(f"{self.year} {self.make} {self.model} has been rented for {days} days.")
        charge = self.rate * float(days)
        print(f"Customer will be charged ${charge:.2f} at return.")

    def set_returned(self):
        self.isRented = False
        print(f"{self.year} {self.make} {self.model} has been returned.")

    def info(self):
        if self.isRented:
            print(f"{self.year} {self.make} {self.model} - RENTED")
        else:
            print(f"{self.year} {self.make} {self.model} - AVAILABLE , PER DAY RATE: ${self.rate}")

class OwlRental:
    def __init__(self):
        self.depot = []

    def add_car(self, make, model, year, rate):
        car = Car(make, model, year, rate)
        self.depot.append(car)

    def list_cars(self):
        for index, car in enumerate(self.depot):
            print(f"{index} - ", end= "")
            car.info()

    def rent_car(self, index, car):
        car = self.depot[index]
        if not car.is_available():
            print("Error: Car is already rented.")
        else:
            car.set_rented(days)

    def return_car(self, index):
        car = self.depot[index]
        if car.is_available():
            print("Error: Car is not rented")
        else:
            car.set_returned()

rental = OwlRental()
rental.add_car("Toyota", "Corolla", 2025, 49.99)
rental.add_car("Honda", "Civic", 2023, 45.50)
rental.add_car("Tesla", "Model 3", 2023, 119.00)

while True:
    print("[Owl Rent-a-Car]")
    print("1. Rent")
    print("2. Return")
    print("3. View cars")
    print("4. Exit")
    choice = input("> ")

    if choice == "1":
        rental.list_cars()
        idx = int(input("select an index: "))
        days = int(input("How many day(s)?: "))
        rental.rent_car(idx, days)

    elif choice == "2":
        rental.list_cars()
        idx = int(input("select an index: "))
        rental.return_car(idx)

    elif choice == "3":
        rental.list_cars()

    elif choice == "4":
        break

    print()



