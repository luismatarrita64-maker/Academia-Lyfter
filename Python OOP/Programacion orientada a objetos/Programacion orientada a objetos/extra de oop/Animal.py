class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "make a sound"


class Dog(Animal):  
    def speak(self): 
        return "Guau"


class Cat(Animal):  
    def speak(self):  
        return "Miau"

d = Dog("set")
c = Cat("pip")

print(d.speak())   
print(c.speak())   