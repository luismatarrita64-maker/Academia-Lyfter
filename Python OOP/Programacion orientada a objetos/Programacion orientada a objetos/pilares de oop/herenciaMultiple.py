class Flyer:
    def fly(self):
        return "I'm flying!"

class Swimmer:
    def swim(self):
        return "I'm swimming!"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly())
print(d.swim())