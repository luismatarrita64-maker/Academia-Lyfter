class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []   

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for p in self.products:
            print(f"Name: {p.name}, Price: {p.price}, Quantity: {p.quantity}")

    def total_value(self):
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total
        
inv = Inventory()


p1 = Product("Apple", 1.20, 30)
p2 = Product("Laptop", 999.99, 3)

inv.add_product(p1)
inv.add_product(p2)
inv.show_products()

print("Total inventory value:", inv.total_value())