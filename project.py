import pandas as pd
# #this is the outline with the total of three classes Kendrick said this would be good to get all the classes done
class User:
  def __Get_User_Info__(self):
    Search_Date = ""
    user_input = input("Enter a NFL team name: ")
    Team_File = pd.read_csv(user_input +".csv")
    User_Choice= input("Press 1 if you want to see season team info: , Press 2 if you want to see a specific dates info: ,Press 3 if you want to see the team's total point over the season")
    if User_Choice == 2: 
        Search_Date = input("Enter the date you want to look at: ")
        print(
            user_input)
        print(User_Choice)
        return [Team_File,User_Choice,Search_Date] and User_Choice




class Get_Info(User):
  def __init__(self):
    self.details = self.__Get_User_Info__()
    self.Team_File = self.details[0]
    self.User_Choice = self.details[1]
    self.Search_Date = self.details[2]



class Main(User):
    def Get_All_Data(self):
        return  self.Team_File
    def Get_Date(self): 
        Date_Location=self.Team_File[self.Team_File.Date.str.contains(self.Search_Date)]
        return Date_Location
    
    # def Get_Regular_Season_Total_Points(self): 
    #     Total_Score=0
    #     if self.Home_Team== team_name:
    #         return team_name



 # #    class Export_Info(Print_Info)

