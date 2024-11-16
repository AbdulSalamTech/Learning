class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passanger = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passanger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passanger)
    

flight = Flight(4)
names = ["abs", "as", "jhon", "david", "hammond"]

for name in names:
    success = flight.add_passanger(name)
    if success:
        print(f"{name} got ticket successfully")
    else:
        print(f"Seats are not available. {name}")

