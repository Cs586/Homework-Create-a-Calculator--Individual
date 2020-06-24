def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(b) - float(a)


def division(a, b):
    c = int(b) / int(a)
    return round(c, 9)


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
