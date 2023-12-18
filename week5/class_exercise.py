class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)
    def area(self):
        return self.length*self.width
        
    def perimeter(self):
        return 2*(self.length+self.width)
        
    
rectangle1 = Rectangle(4,5)
print(f"area= {rectangle1.area()} and perimeter= {rectangle1.perimeter()}" )