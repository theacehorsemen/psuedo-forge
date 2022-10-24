#Program to override functions and code operations on complex numbers
import cmath

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def __add__(self, no):
        rl = self.real + no.real
        im = self.imag + no.imag
        return Complex(rl, im)
        
    def __sub__(self, no):
        rl = self.real - no.real
        im = self.imag - no.imag
        return Complex(rl, im)
        
    def __mul__(self, no):
        res = complex(self.real, self.imag) * complex(no.real, no.imag)
        return Complex(res.real, res.imag)        

    def __truediv__(self, no):
        res = complex(self.real, self.imag) / complex(no.real, no.imag)
        return Complex(res.real, res.imag)
        
    def mod(self):
        res = math.sqrt(self.real**2 + self.imag**2)
        return Complex(res, 0)
        

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result


