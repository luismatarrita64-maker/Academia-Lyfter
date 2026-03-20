class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got on the bus")
        else:
            print("The bus is full")

    def remove_passenger(self):
        if self.passengers:
            person = self.passengers.pop()
            print(f"{person.name} got off the bus")
        else:
            print("There are no passengers on the bus")



p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

bus = Bus(2)

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger(p3)   

bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()  