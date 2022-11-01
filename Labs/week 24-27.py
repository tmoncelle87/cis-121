# from cat import Cat


# test = Cat("Robbie")

# test.displayInfo()
import random

#Parent Class
class Student:
  def __init__(self,name,lastname):
    self.name = name
    self.lastname = lastname
    #data encuapsulation
    self.__ssn = random.randint(1000000000,9999999999)
    
  #Poly
  def displayInfo(self):
    print(f"Name: {self.name}")
    print(f"Lastname: {self.lastname}")
    print(f"SSN: {self.__ssn}")

  def getSSN(self):
    return self.__ssn

#Child Class
#Inhe 
class HighSchoolStudent(Student):
  def __init__(self,name,lastname,grade):

    super().__init__(name,lastname)
    self.grade = grade

  #pOLY
  def displayInfo(self):
    print(f"Name: {self.name}")
    print(f"Lastname: {self.lastname}")
    print(f"SSN: {self.getSSN()}")
    print(f"Grade: {self.grade}")


student = Student("Bob","Boberson")

student2 = HighSchoolStudent("Rob","Robertson",10)

student.displayInfo()
student2.displayInfo()
#work on this over weekend
