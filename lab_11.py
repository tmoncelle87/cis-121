


class Employee:
    def __init__(self,name,id_):
        self.name=name
        self.id_ = id_
class Salary_Employee(Employee):
    def __init__(self, name,Weekly_Salary,id_):
        self.Weekly_Salary=Weekly_Salary
        super().__init__(name,id_)
    def Calculate_Yearly_Salary(self):
        Yearly_Salary=(self.Weekly_Salary * 52)
        return Yearly_Salary
    def Print_Salary_Yearly(self):
        print(Tony.Calculate_Yearly_Salary())
class Hourly_Employee(Employee):
    def __init__(self, name,Hourly_Pay,Weekly_Hours,id_):
        self.Hourly_Pay=Hourly_Pay
        self.Weekly_Hours=Weekly_Hours
        super().__init__(name,id_)
    def Calulate_Yearly_Pay(self):
        Total= (self.Hourly_Pay * self.Weekly_Hours * 52)
        return Total
    def Print_Yearly_Hourly_Salary(self):
        print(Ray.Calulate_Yearly_Pay())
class Commission_Employee(Salary_Employee):
    def __init__(self, name,Commission,id_,Weekly_Salary):
        self.Commission=Commission
        super().__init__(name,Weekly_Salary,id_)
    def Calculate_Yearly_Salary_Commission(self):
        Total_Yearly_Commission=(self.Commission+ super().Calculate_Yearly_Salary())
        return Total_Yearly_Commission
    def Print_Yearly_Commission_Salary(self):
        print(Kendrick.Calculate_Yearly_Salary_Commission())



Kendrick=Commission_Employee("Kendrick",5000000000,10,.000000000001)
Kendrick.Print_Yearly_Commission_Salary()
Ray=Hourly_Employee("Ray",20,20,200)
Ray.Print_Yearly_Hourly_Salary()
Tony=Salary_Employee('Tony',785,8)
Tony.Print_Salary_Yearly()
