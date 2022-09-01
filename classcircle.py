import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = math.pi * (self.radius ^ 2)
        print(f'The area of the circle is {self.area}')

    def perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        print(f'The perimeter of the circle is {self.perimeter}')

a = int(input('What is the radius of the circle: '))
x = Circle(a)
x.area()
x.perimeter()