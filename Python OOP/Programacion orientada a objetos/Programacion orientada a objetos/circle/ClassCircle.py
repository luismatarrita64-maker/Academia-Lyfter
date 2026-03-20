class circle :
    radius = 10

    def get_area(self):
        area = 3.14 * self.radius **2

        print(area)

my_circle = circle()
my_circle.get_area()