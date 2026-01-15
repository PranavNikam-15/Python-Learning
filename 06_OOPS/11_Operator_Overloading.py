# Operator overloading allows same operator to work in different ways depending on data type.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, P):
        return Point((self.x + P.x), (self.y + P.y))
    
    def display_point(self):
        print(f"X = {self.x} & Y = {self.y}")

    def __add__(self, P):
        return Point((self.x + P.x), (self.y + P.y))

    
P1 = Point(5, 15)
P2 = Point(11, 22)

# Returns a new point which is sum of both points
P = P1.sum(P2) 

# Overloaded + operator by writing __add__ function
P = P1 + P2

P.display_point()