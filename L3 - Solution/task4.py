# Parent class that contain all attributes that will be used by classes Pants and Shirt
class Clothing:
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        print("Name:", self.name)
        print("Size:", self.size)
        print("Color:", self.color)
        print("Price:", self.price)

class Shirt(Clothing):
    def __init__(self, name, size, color, price, type):
        # super() method helps you to use methods of Parent class (Clothing)
        super().__init__(name, size, color, price)
        self.type = type

    def display_info(self):
        super().display_info()
        print("Type:", self.type)

class Pants(Clothing):
    def __init__(self, name, size, color, price, length):
        super().__init__(name, size, color, price)
        self.length = length

    def display_info(self):
        super().display_info()
        print("Length:", self.length)

# Example usage
shirt = Shirt("T-Shirt", "L", "Blue", 25.0, "Casual")
shirt.display_info()
# Output:
# Name: T-Shirt
# Size: L
# Color: Blue
# Price: 25.0
# Type: Casual

pants = Pants("Jeans", "M", "Blue", 50.0, "Regular")
pants.display_info()
# Output:
# Name: Jeans
# Size: M
# Color: Blue
# Price: 50.0
# Length: Regular