# class Point has methods and attributes that describes it.
class Point:
    # `self` can be changed to anything but for convinience is used as `self`.
    # `self` gives you access to the methods and attributes of its class (Point)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    # `other` is same as self refers to the point2. point2 is object of class Point.
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return (dx**2 + dy**2)**0.5

    # Useful method where you can show how object is look like.
    # For example: Point has x and y => Point(x,y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(10,4)
point2 = Point(5,12)

print(point1.distance(point2))
point1.shift(10,1)
print(point1.distance(point2))
print(point2.__str__())