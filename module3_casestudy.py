# Vehicle Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Automobile Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Gets user input and creates an instance of Automobile. Finally, outputs the data.
def main():
    print("Welcome to the Car Information Database! Please enter the following information about your car so it can be stored: \n")

    vehicle_type = "car"  # Only one input acceptable for this case study
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("How many doors? (2 or 4): ")
    roof = input("What type of roof? (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

if __name__ == "__main__":
    main()