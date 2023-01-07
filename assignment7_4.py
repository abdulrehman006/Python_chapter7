"""
Create a class Rectangle. The class has attributes __length and __width, each of
which defaults to 1. It has methods that calculate the perimeter and the area of the
rectangle. It has set and get methods for both __length and __width. The set methods
should verify that __length and __width are each floating-point numbers larger than
0.0 and less than 20.0. Write a driver program to test the class.
"""

class Rectangle:
    def __init__(self, length=1, width=1):
        self.__length = length
        self.__width = width

    def set_length(self, length):
        if length > 0.0 and length < 20.0:
            self.__length = length
        else:
            raise ValueError("Length must be between 0.0 and 20.0")

    def set_width(self, width):
        if width > 0.0 and width < 20.0:
            self.__width = width
        else:
            raise ValueError("Width must be between 0.0 and 20.0")

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width


rect = Rectangle(2, 4)
print(f'Length: {rect.get_length()}')
print(f'Width: {rect.get_width()}')
print(f'Area: {rect.area()}')
print(f'Perimeter: {rect.perimeter()}')

rect.set_length(5)
rect.set_width(10)
print(f'Length: {rect.get_length()}')
print(f'Width: {rect.get_width()}')
print(f'Area: {rect.area()}')
print(f'Perimeter: {rect.perimeter()}')