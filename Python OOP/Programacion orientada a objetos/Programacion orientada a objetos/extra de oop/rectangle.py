class rectangle :

    def __init__(self):
        try :

            self.width = float(input("Enter the width: "))
            self.height = float(input("Enter the height: "))

        except ValueError:  
            raise ValueError("cant be a negative number or letter")
        
            
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height cannot be negative.")

    def get_area(self):  
            return self.width * self.height

    def get_perimeter(self):
            return 2 * (self.width + self.height)



my_rectangle = rectangle()
print("Area:", my_rectangle.get_area())
print("Perimeter:", my_rectangle.get_perimeter())