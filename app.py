class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if self.capacity == 0:
            print("Flight is full")
        else:
            self.passengers.append(name)
    
    def number_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(32)

print(flight.capacity)

print(flight.passengers)


person = ["John", "Jane", "Doe"]

for p in person:
    success = flight.add_passenger(p)
    if success == True:
        print(f"Added {p} to the flight")
    else:
        print(f"Could not add {p} to the flight due to overcpacity ")

