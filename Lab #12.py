import random
class Company:
    def __init__(self,Name,Year):
        self.Name=Name
        self.Year= Year
class Car:
    def __init__(self,Wheels,Company,Color,Miles,Status,Speed):
        self.Wheels=Wheels
        self.Company=Company
        self.Color=Color
        self.Miles=Miles
        self.Status=Status
        self.Speed=Speed
    def Acceleration(self,Amount):
        self.Speed += Amount
        self.Status= "Accelerating"
        self.Update_Miles(Amount)
    def Update_Miles(self,Amount):
        if self.Status== "Accelerating":
            self.Miles += Amount
    def Stop(self):
        self.Status="Stopped"
        self.Speed= 0      
    def Decrease(self):
        self.Speed -=20

        if self.Speed < 0:
            self.Speed = 0

        self.Status="Slowing Down"




def ZerotoSixty():
    company=Company("Nissan",1920)
    car1=Car(4,company,"Blue",0,"Stopped",0)
    car1=Car(4,company,"Red",0,"Stopped",3)
    car1=Car(4,company,"Black",40,"Stopped",50)
    car1=Car(4,company,"Pink",25,"Stopped",0)
    car1=Car(4,company,"Purple",1000000,"Stopped",99)
    Reached60 = False
    secconds=0
    while Reached60 != True:
        secconds +=1
        car1.Acceleration(random.randint(1,25))
        if car1.Speed >=60:
            Reached60=True
    print("=====Run   Info====")
    print("took "+ str(secconds),"secconds to reach 0-60 mph")
    print("It ran" +str(car1.Miles))


ZerotoSixty()
def Zeroto100():
    company=Company("Nissan",1920)
    car1=Car(4,company,"Blue",0,"Stopped",10)
    car2=Car(4,company,"Red",0,"Stopped",60)
    car3=Car(4,company,"Black",0,"Stopped",30)
    car4=Car(4,company,"Pink",0,"Stopped",20)
    car5=Car(4,company,"Purple",0,"Stopped",25)
    Reached100 = False
    secconds=0
    while Reached100 != True:
        secconds +=1
        car1.Acceleration(random.randint(1,25))
        car2.Acceleration(random.randint(1,25))
        car3.Acceleration(random.randint(1,25))
        car4.Acceleration(random.randint(1,25))
        car5.Acceleration(random.randint(1,25))
        if car1.Speed>=100:
            Reached100=True
    print("=====Run   Info====")
    print("took "+ str(secconds),"secconds to reach 0-100 mph")
    print("Car 1 ran " +str(car1.Miles) + " Miles ")
Zeroto100()
def Zeroto250():
    company=Company("Nissan",1920)
    car1=Car(4,company,"Blue",0,"Stopped",10)
    car2=Car(4,company,"Red",0,"Stopped",60)
    car3=Car(4,company,"Black",0,"Stopped",30)
    car4=Car(4,company,"Pink",0,"Stopped",20)
    car5=Car(4,company,"Purple",0,"Stopped",25)
    Reached250 = False
    secconds=0
    while Reached250 != True:
        secconds +=1
        car1.Acceleration(random.randint(1,25))
        car2.Acceleration(random.randint(1,25))
        car3.Acceleration(random.randint(1,25))
        car4.Acceleration(random.randint(1,25))
        car5.Acceleration(random.randint(1,25))
        if car1.Speed >=250:
            Reached250=True
    print("=====Run   Info====")
    print("took "+ str(secconds),"secconds to reach 0-250 mph")
    print("Car 1 ran " +str(car1.Miles) + " Miles ")
Zeroto250()
#create 5 different cars and check 0-100 and 0-250 and display amount of miles ran