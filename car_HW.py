class Cars:
    def __init__(self, door, salon, passenger_place, wheels):
        self.door = door
        self.salon = salon
        self.passenger_place = passenger_place
        self.wheels = wheels

    def data(self):
        door1 = {
            2: ["chevrolet camaro", "BMW 2 Series", "BMW M4", "chevrolet coverette"],
            4: ["Nexia 1", "Nexia 2", "Nexia 3", "Lacetti"]
        }
        salon1 = {
            'sport': ['chevrolet camaro', 'BMW 2 Series', 'BMW M4', 'chevrolet coverette'],
            'daily': ['Nexia 1', 'Nexia 2', 'Nexia 3', 'Lacetti'],
            'luxry': ['chevrolet camaro', 'BMW 2 Series', 'BMW M4', 'chevrolet coverette']
        }
        passenger_place1 = {
            2: ['chevrolet camaro', 'BMW 2 Series', 'BMW M4', 'chevrolet coverette'],
            5: ['Nexia 1', 'Nexia 2', 'Nexia 3', 'Lacetti']
        }

        cars_by_door = door1.get(self.door, [])
        cars_by_salon = salon1.get(self.salon, [])
        cars_by_passenger_place = passenger_place1.get(self.passenger_place, [])

        available_cars = set(cars_by_door) & set(cars_by_salon) & set(cars_by_passenger_place)

        return list(available_cars)

# Get user input for car criteria
door = int(input("Number of doors: "))
salon = input("Salon type (sport/daily/luxry): ")
passenger_place = int(input("Number of passenger places: "))
wheels = int(input("Number of wheels: "))

car_search = Cars(door, salon, passenger_place, wheels)
result = car_search.data()

if result:
    print("Available cars:")
    for car in result:
        print("-", car)
else:
    print("No cars available with the specified criteria.")
