import math

def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(b) - float(a)


def division(a, b):
    c = int(b) / int(a)
    return round(c, 9)


def mul(a, b):
    return int(a) * int(b)


def sq(a):
    return int(a)**2

def sqr(a):
    return math.sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def mul(self, a, b):
        self.result = mul(a, b)
        return self.result

    def sq(self, a, b):
        self.result = sq(a)
        return self.result

    def sqr(self):
        self.result = sqr(a)
        return self.result