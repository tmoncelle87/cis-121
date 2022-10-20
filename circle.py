import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        return (self.radius**2)*math.pi
    def calculatePeremeter(self):
        return (self.radius*math.pi)*2

    def __str__(self):
        print("====Circle===")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.calculateArea()}")
        print(f"Perimeter: {self.calculatePeremeter()}")
        return ""