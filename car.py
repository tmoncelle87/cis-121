#function inside a class is called a method
#self has to be in function
class Car:
    def __init__(self,number_of_wheels,engine,model,year):
        self.number_of_wheels = number_of_wheels
        self.engine= engine
        self.model=model
        self.year = year
    def change_year(self,new_year):
        self.year = new_year
    def change_engine(self,new_engine):
        self.engine=new_engine
    def change_model(self,new_model):
        self.model=new_model
    def change_number_of_wheels(self,new_number_of_wheels):
        self.number_of_wheels=new_number_of_wheels
    def __str__(self):
        print("======Car  Info====")
        print(f"model: {self.model}")
        print(f"engine: {self.engine}")
        print(f"year: {self.year}")
        print(f"number of wheels: {self.number_of_wheels}")
        return ""