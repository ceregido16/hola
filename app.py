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