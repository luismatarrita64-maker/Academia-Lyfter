class Circle :

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * self.radius **2
        return area
        

MyCircle = Circle(10)
print("Area : ",MyCircle.get_area())