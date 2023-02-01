import pandas as pd


#class get info gets all the information needed from user
class GetInfo:

  def Get_Date(self, file, date):
    Date_Location = file[file.Date.str.contains(date)]
    return Date_Location

  def UserInput(self, inp):
    userinput = input(inp)
    return userinput

  def TeamFile(self, file):
    Team_File = pd.read_csv(f"{file}.csv")
    return Team_File

  def UserChoice(self, choice):
    userchoice = int(input(choice))
    return userchoice

  def Get_Team_Info(self):
    user_input = GetInfo().UserInput("Enter a NFL team name: ")
    return GetInfo().TeamFile(user_input)

  def Get_Team_By_Date(self):
    Search_Date = input("Enter the date you want to look at: ")
    user_input = GetInfo().UserInput("Enter a NFL team name: ")
    Team_File = GetInfo().TeamFile(user_input)
    info = self.Get_Date(Team_File, Search_Date)
    return info

  # Requests team name and print out score card for each game.
  def Get_Team_Total(self):
    user_input = GetInfo().UserInput("Enter a NFL team name: ")
    Team_File = GetInfo().TeamFile(user_input)

    df = pd.DataFrame(Team_File)

    score_list = []
    counter = 0
    while counter < 30:
      try:
        score_list.append(df.loc[counter][6])
        counter += 1
      except:
        break
    return score_list

  #this method prints out team information based on user choice
  def Get_User_Info(self):
    Search_Date = ""

    user_input = GetInfo().UserInput("Enter a NFL team name: ")
    Team_File = GetInfo().TeamFile(user_input)
    User_Choice = GetInfo().UserChoice(
      "Enter 1 if you want to see season team info: , Enter 2 if you want to see a specific date info: , Enter 3 if you want to see the team's score each game: "
    )

    if User_Choice == 1:
      print(User_Choice)
      print(user_input)
      print(Team_File)

    if User_Choice == 2:
      Search_Date = input("Enter the date you want to look at: ")
      info = self.Get_Date(Team_File, Search_Date)
      print(User_Choice)
      print(user_input)
      print(info)

    if User_Choice == 3:
      df = pd.DataFrame(Team_File)
      dates_list= []
      score_list = []
      
      counter = 0
      while counter < 30:
        try:
          score_list.append(df.loc[counter][6])
          dates_list.append(df.loc[counter][2])
          
          counter += 1
        #expection when error happens, loop ends
        except:
          break
      for i in range(len(score_list)):
        print((dates_list)[i]+(" ")+(score_list)[i])

    return [Team_File, User_Choice, Search_Date]


class User:

  def __init__(self):
    self.details = GetInfo().Get_User_Info()
    self.Team_File = self.details[0]
    self.User_Choice = self.details[1]
    self.Search_Date = self.details[2]


class Main:

  def Get_All_Data(self):
    user_input = GetInfo().UserInput("Enter a NFL team name: ")
    return GetInfo().TeamFile(user_input)

  def Get_Regular_Season_Total_Points(self):
    return GetInfo().Get_Team_Total()

  def PrintTeamInfo(self):
    print("=== Team Info ===")
    print(GetInfo().Get_Team_Info())

  def PrintSpecificDateInfo(self):
    print("=== Date Information ===")
    print(GetInfo().Get_Team_By_Date())

  def PrintRegularSeasonTotal(self):
    print("=== Total Season Points ===")
    print(Main().Get_Regular_Season_Total_Points())


class ExportInfo():

  def ExportAllTeamInfo(self):
    Team_File = GetInfo().Get_Team_Info()
    with open("results_all_info.txt", 'w') as f:
      f.write(f"The Team Information is: {str(Team_File)}")

  def ExportSpecificDateLocation(self):
    Team_By_Date = GetInfo().Get_Team_By_Date()
    with open("results_date_info.txt", 'w') as f:
      f.write(f"The Specific Date Info is: {str(Team_By_Date)}")

  def ExportRegularSeasonPoints(self):
    Team_Total = Main().Get_Regular_Season_Total_Points()
    with open("results_season_info.txt", 'w') as f:
      f.write(
        f"The team's total points over the season was: {str(Team_Total)}")


# run code
GetInfo().Get_User_Info()

# call class main and functions to print information
#Main().PrintTeamInfo()
#Main().PrintSpecificDateInfo()
#Main().PrintRegularSeasonTotal(
