from abc import ABC,abstractmethod  

class Shape (ABC):

    @abstractmethod

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass



class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius **2
    

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    
class Rectangle (Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height


    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

        
class Square(Rectangle):  # hasta matematicas tuve que estudiar para hacer este jaja
    def __init__(self, side):
        super().__init__(side, side)


my_circle = Circle(10)
print("Circle")
print("Area =" ,my_circle.calculate_area())
print("Perimeter =",my_circle.calculate_perimeter())

print("------------------------------------")

my_rectangle = Rectangle(21,98)
print("Rectangle")
print("Area =" ,my_rectangle.calculate_area())
print("Perimeter =",my_rectangle.calculate_perimeter())

print("------------------------------------")

my_square = Square(17)
print("Square")
print("Area =" ,my_square.calculate_area())
print("Perimeter =",my_square.calculate_perimeter())