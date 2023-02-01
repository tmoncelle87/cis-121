#Tony Moncelle 11/21/2022
#1 Implement
class Vehicle:
    def __init__(self,NumPassengers:int,Manufacturer:str,NumWheels:int):
        self.NumPassengers=NumPassengers
        self.Manufacturer=Manufacturer
        self.NumWheels=NumWheels
class AutoMobile(Vehicle):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int,MPG:float,Model:str,NumDoors:int):
        super().__init__(NumPassengers, Manufacturer, NumWheels)
        self.MPG=MPG
        self.Model=Model
        self.NumDoors=NumDoors
class TwoWheeler(Vehicle):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int,Model:str,Weight:int):
        super().__init__(NumPassengers, Manufacturer, NumWheels)
        self.Model=Model
        self.Weight=Weight
class Sedan(AutoMobile):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int, MPG: float, Model: str, NumDoors: int,Type:str,NumCylinders:int,HorsePower:float):
        super().__init__(NumPassengers, Manufacturer, NumWheels, MPG, Model, NumDoors)
        self.Type=Type
        self.NumCylinders=NumCylinders
        self.HorsePower=HorsePower
class Truck(AutoMobile):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int, MPG: float, Model: str, NumDoors: int,Type:str,NumAxels:int,MaxTowPayload:int):
        super().__init__(NumPassengers, Manufacturer, NumWheels, MPG, Model, NumDoors)
        self.Type=Type
        self.NumAxels=NumAxels
        self.MaxTowPayload=MaxTowPayload
class Motorcycle(TwoWheeler):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int, Model: str, Weight: int,Type:str,MPG:float,HorsePower:int):
        super().__init__(NumPassengers, Manufacturer, NumWheels, Model, Weight)
        self.Type=Type
        self.MPG=MPG
        self.HorsePower=HorsePower
class Bicycle(TwoWheeler):
    def __init__(self, NumPassengers: int, Manufacturer: str, NumWheels: int, Model: str, Weight: int,HasGears:bool,HasSuspension:bool,WheelSize:float):
        super().__init__(NumPassengers, Manufacturer, NumWheels, Model, Weight)
        self.HasGears=HasGears
        self.HasSuspension=HasSuspension
        self.WheelSize=WheelSize
#2: 
# What I can figure out from the diagram is that there are three parent classes. 
# Vehicle is a parent class to AutoMobile and TwoWheeler. 
# AutoMobile and TwoWheeler are ntoh child classes of Vehicle. 
# Automobile is a parent class to Sedan and Truck which are both child classes. 
# TwoWheeler is a parent class to Motorcycle and Bicycle which are both child classes.


#3
class Customer:
    def MakePurchase(self,Amount:int):
        self.Amount=Amount
    def DiscountReached(self):
        total=0
        if self.Amount >= 100:
           total= self.Amount -100 -10 
           return total
Tony=Customer(110)
print(Tony)
