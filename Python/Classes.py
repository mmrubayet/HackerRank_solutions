import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, no):
        a=self.real+no.real
        b=self.imaginary+no.imaginary
        return Complex(a,b)

    def __sub__(self, no):
        a=self.real-no.real
        b=self.imaginary-no.imaginary
        return Complex(a,b)

    def __mul__(self, no):
        a=(self.real*no.real) - (self.imaginary*no.imaginary)
        b=(self.real*no.imaginary) + (self.imaginary*no.real)
        return Complex(a,b)

    def __truediv__(self, no):
        d = (no.real* no.real) +(no.imaginary*no.imaginary)
        a=((self.real*no.real) + (self.imaginary*no.imaginary))/d
        b=((self.imaginary*no.real) - (self.real*no.imaginary))/d
        return Complex(a,b)

    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a**2+b**2),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
