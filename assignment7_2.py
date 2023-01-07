"""
Create a class called RationalNumber for performing arithmetic with fractions.
(Write a driver program to test your class.)
Use integer variables to represent the data of the class—the numerator and the
denominator. Provide a constructor that enables an object of this class to be initialised
when it is declared. The constructor should contain default values, in case no initializers
are provided, and should store the fraction in reduced form (i.e., the fraction
2/4
would be stored in the object as 1 in the numerator and 2 in the denominator). Provide
methods for each of the following:
a) Adding two RationalNumbers. The result should be stored in reduced form.
b) Subtracting two RationalNumbers. The result should be stored in reduced form.
c) Multiplying two RationalNumbers. The result should be stored in reduced form.
d) Dividing two RationalNumbers. The result should be stored in reduced form.
e) Printing RationalNumbers in the form a/b, where a is the numerator and b is the
denominator.
f) Printing RationalNumbers in floating-point format.
"""
class RationalNumber:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()
    
    def reduce(self):
        """Reduce the fraction to its simplest form."""
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
    
    def gcd(self, a, b):
        """Find the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        """Add two RationalNumbers."""
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)
    
    def __sub__(self, other):
        """Subtract two RationalNumbers."""
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)
    
    def __mul__(self, other):
        """Multiply two RationalNumbers."""
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)
    
    def __truediv__(self, other):
        """Divide two RationalNumbers."""
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return RationalNumber(numerator, denominator)
    
    def __str__(self):
        """Print the fraction in the form a/b."""
        return f"{self.numerator}/{self.denominator}"
    
    def to_float(self):
        """Print the fraction as a floating-point number."""
        return self.numerator / self.denominator

if __name__ == "__main__":
    # Create some RationalNumber objects
    r1 = RationalNumber(2, 4)
    r2 = RationalNumber(3, 6)
    r3 = RationalNumber(4, 8)
    r4 = RationalNumber(5, 10)
    
    # Perform some operations
    r5 = r1 + r2
    r6 = r3 - r4
    r7 = r1 * r2
    r8 = r3 / r4
    
    # Print the results
    print(r5)  # 1/2
    print(r6)  #
