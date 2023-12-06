class Vehicle:
    def __init__(self, y, m, mo):
        self.year = y 
        self.make = m
        self.model = mo
    def to_string(self):
        return "{} {} {}".format(self.year, self.make, self.model)