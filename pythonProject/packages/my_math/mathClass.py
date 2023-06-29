from packages.my_math import calc as c


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return c.add(self.a, self.b)

    def sub(self):
        return c.sub(self.a, self.b)

    def mul(self):
        return c.mul(self.a, self.b)

    def div(self):
        return c.div(self.a, self.b)
