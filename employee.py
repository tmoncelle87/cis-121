class Employee:
    def __init__(self,hour_pay,weekly_hours,name_,position,yearly_salary):
        self.hour_pay= hour_pay
        self.weekly_hours= weekly_hours
        self.name = name_
        self.position=position
        self.yearly_salary= yearly_salary
    def change_hourly_pay(self,new_hourly_pay):
        self.weekly_hours = new_weekly_hours
    def change_name(self,new_name):
        self.name=new_name
    def change_position(self,new_position):
        self.position=new_position
    def change_yearly_salary(self,new_yearly_salary):
        self.yearly_salary=new_yearly_salary
    def __str__(self):
        print("======Employee====")
        print(f"hourly pay: {self.hour_pay}")
        print(f"weekly hours: {self.weekly_hours}")
        print(f"name: {self.name}")
        print(f"occupation: {self.position}")
        print(f"yearly salarly: {self.weekly_hours *self.hour_pay * 48}")
        return ""
