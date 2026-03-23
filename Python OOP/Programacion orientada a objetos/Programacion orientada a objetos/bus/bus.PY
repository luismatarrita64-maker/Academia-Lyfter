class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if not isinstance(person, Person):
            raise TypeError("The passenger must be an instance of Person")
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got on the bus")
        else:
            raise Exception("The bus is full")

    def remove_passenger(self):
        if not self.passengers:
            raise Exception("There are no passengers on the bus")
        person = self.passengers.pop()
        print(f"{person.name} got off the bus")


p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")

bus = Bus(2)

bus.add_passenger(p1)
bus.add_passenger(p2)

try:
    bus.add_passenger(p3)
except Exception as e:
    print(e)

bus.remove_passenger()
bus.remove_passenger()

try:
    bus.remove_passenger()
except Exception as e:
    print(e)