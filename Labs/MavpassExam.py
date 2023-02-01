# class penguin:
#     def __init__(self,Size,Color,Age):
#         self.Size=Size
#         self.Color=Color
#         self.Age=Age
#     def GetSize(self):
#         return self.Size
#     def GetColor(self):
#         return self.Color
#     def GetAge(self):
#         return self.Age
#     def ChangeAge(self,NewAge):
#         self.Age=NewAge
# Penguin=penguin(55,"red",70)
# print(Penguin.GetAge())
# Penguin.ChangeAge(10)
# print(Penguin.GetAge())
# class Fin(penguin):
#     def __init__(self, Size,Age,Color,Length):
#         super().__init__(Size, Age,Color)
#         self.Length=Length
#     def GetNewSize(self):
#         return super().GetSize()

# fin=Fin(11,20,"red",12)
# print(fin.GetNewSize())

# class Whale:
#     def __init__(self,Size:str,Color:str,Gender:str):
#         self.Size=Size
#         self.Color=Color
#         self.Gender=Gender
# class BlueWhale(Whale):
#     def __init__(self, Size, Color, Gender):
#         super().__init__(Size, Color, Gender)
#     def __str__(self):
#         return f"{self.Gender},{self.Color},{self.Size}"
# blue=BlueWhale("100 meters","red","male")
# print(blue)
# class Fox:
#     def __init__(self,Age:int,Color:str="red"):
#         self.Color=Color
#         self.Age=Age
#     def __str__(self):
#         return f"{self.Age},{self.Color}"

# f=Fox(17,"blue")
# print(f)


def ChangeROmanNumerial():
    dicti={
    "I":1,
    "V": 5,
    "X": 10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    }
    RomanNumerials="MV"
    RomanNumerials = RomanNumerials.replace("IV","IIII").replace("IX","VIIII")
    RomanNumerials = RomanNumerials.replace("XL","XXXX").replace("XC","LXXXX")
    RomanNumerials = RomanNumerials.replace("CD","CCCC").replace("CM","DCCCC")
    Total=0
    for Zebra in RomanNumerials:
        Total+=dicti[Zebra]
    print(Total)
ChangeROmanNumerial()