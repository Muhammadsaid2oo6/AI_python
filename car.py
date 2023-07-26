
def identify_car(door, passenger_place, wheels):
    car_data = {
        (2, 2, 4): 'Sedan, BMW M4, BMW 2-Series, Camaro, Corvette, McLaren ',
        (4, 8, 4): 'Nissan, Renault, eVito, Peugeot',
        (4, 4, 4): 'Exter, Thar, Seltos, Nexon',
        (2, 16, 4): 'BUS',
        (3, 2, 2): 'Isetta',
    }
    keys = (door, passenger_place, wheels)
    return car_data.get(keys)


door = int(input("Eshiklar soni: "))
passenger_place = int(input("O'rindiqlar soni: "))
wheels = int(input("G'ildiraklar soni:  "))

car = identify_car(door, passenger_place, wheels)

print(f"The car is identified as: {car}")



