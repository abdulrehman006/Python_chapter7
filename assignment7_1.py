"""
Create a class called Complex for performing arithmetic with complex numbers.
Write a driver program to test your class.
Complex numbers have the form
realPart + imaginaryPart * i
where i is ( square root of -1 ) or √(−1)
Use floating-point numbers to represent the data of the class. Provide a constructor that
enables an object of this class to be initialised when it is created. The constructor should
contain default values in case no initializers are provided. Provide methods for each of
the following:
a) Adding two ComplexNumbers: The real parts are added to form the real part of the
result, and the imaginary parts are added to form the imaginary part of the result.
b) Subtracting two ComplexNumbers: The real part of the right operand is subtracted
from the real part of the left operand to form the real part of the result, and the
imaginary part of the right operand is subtracted from the imaginary part of the left
operand to form the imaginary part of the result.
c) Printing ComplexNumbers in the form (a, b), where a is the real part and b is the
imaginary part.
"""

class Complex:
  def __init__(self, real=0, imaginary=0):
    self.real = real
    self.imaginary = imaginary
    
  def add(self, other):
    result = Complex()
    result.real = self.real + other.real
    result.imaginary = self.imaginary + other.imaginary
    return result
  
  def subtract(self, other):
    result = Complex()
    result.real = self.real - other.real
    result.imaginary = self.imaginary - other.imaginary
    return result
  
  def __str__(self):
    return "({}, {})".format(self.real, self.imaginary)
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Adding c1 and c2:", c1.add(c2))
print("Subtracting c1 and c2:", c1.subtract(c2))
print("c1:", c1)
print("c2:", c2)
