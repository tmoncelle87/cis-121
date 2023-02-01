#Tony Moncelle Exam Review
#1: What I notice from figure one is that there are 3 child classes which each inherit information from the parent class Person. Person class has an innit method. Address has 6 methods which include an innit and a bunch of get methods. Student class has 3 methods one innit and 2 get methods. Teacher class has 6 methods including 1 innit and 4 get methods and one calculate method. 
#2: Person is the parent class and Address, Student and Teacher are all child classes from the parent class Person because they all inherit information from that class which is name, phone number and email address
#Code is below 
class Person:
    def __init__(self,Name,PhoneNumber,EmailAddress):
        self.Name=Name
        self.PhoneNumber=PhoneNumber
        self.EmailAddress=EmailAddress
class Student(Person):
    def __init__(self,Name,PhoneNumber,EmailAddress,StudentNumber,GPA):
        super().__init__(Name, PhoneNumber, EmailAddress)
        self.StudentNumber=StudentNumber
        self.GPA=GPA
    def GetGPA(self):
        return self.GPA
    def GetStudentNumber(self):
        return self.StudentNumber
class Teacher(Person):
    def __init__(self, Name, PhoneNumber, EmailAddress,TeacherId,WorkHours,WorkRate,YearsOfService):
        super().__init__(Name, PhoneNumber, EmailAddress)
        self.TeacherId=TeacherId
        self.WorkHours=WorkHours
        self.WorkRate=WorkRate
        self.YearsOfService=YearsOfService
    def GetTeacherId(self):
        return self.TeacherId 
    def GetWorkHours(self):
        return self.WorkHours
    def GetWorkRate(self):
        return self.WorkRate
    def GetYearsOfService(self):
        return self.YearsOfService
    def CalculateYearlySalary(self):
        YearlySalary=(self.WorkHours*self.WorkRate*52)
        return YearlySalary 
class Address(Person):
    def __init__(self, Name, PhoneNumber, EmailAddress,Street,City,Country,ZipCode,State):
        super().__init__(Name, PhoneNumber, EmailAddress)
        self.Street=Street
        self.City=City
        self.Country=Country
        self.ZipCode=ZipCode
        self.State=State
        self.Address= str(self.Street)+str(self.City)+str(self.Country)+str(self.ZipCode)+str(self.State)
    def GetAddress(self):
        return self.Address
    def GetCity(self):
        return self.City
    def GetZipCode(self):
        return self.ZipCode
    def GetState(self):
        return self.State
    def GetCountry(self):
        return self.Country
Ton=Person("Tony","911","hm2955zq@go.minnstate.edu")
TonI=Student("Tony","911","hm2955zq@go.minnstate.edu",14,3.2)
Tony=Teacher("Tony","911","hm2955zq@go.minnstate.edu",145,40,15,10)
#This will not display any information just creates a instance

