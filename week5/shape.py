import math

class Shape:
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_area(self):
        return self.width * self.length
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(6)
rectangle = Rectangle(4,5)
triangle = Triangle(3,4)
print(f"Area of a circle is: {circle.calculate_area()}")
print(f"Area of a rectangle is: {rectangle.calculate_area()}")
print(f"Area of a triangle is: {triangle.calculate_area()}")