import random
#this class works and is good to go. The class 

class Die:
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
        self.face_up_value= 1
    def roll(self):
        self.face_value= random.randint[1,self.number_of_sides]
    def getValue(self):
        return self.face_value
    def __str__(self):
        print(f"The number of sides on this dice is: {self.number_of_sides}")
        print(f"The face value is: {self.face_value}")
        return ''
    def __add__(self,die2):
        self.Totals= self.face_value+die2
    def __gt__(self):
        return self.Totals
class Player():
    def __init__(self,name1,die1,die2):
        self.player1= name1
        self.die1 = die1
        self.die2=die2
        self.Totals = self.Totals
    def rollDice(self):
        self.die1.roll()
        self.die2.roll()
    def getDiceValue(self):
        return self.die1.face_value and self.die2.face_value 
    def __str__(self):
        print(f"{self.player1} Total is: {self.Totals}")   
    #everything above is working but I cannot figure out how to get totals in the hightwogame class at all. I have tried returning it and defining it but nothing is working
class HighTwoGame(Player):
    def playOneGame(self):
        print(f"{self.player1} rolled {self.Totals}")
#can't work on this paet yet because im not done with play one game yet     
    def playManygames(number_of_games,):
        Value=0
        while number_of_games > Value:
    def __str__(self):
        print("====Game One====")
        print(f"{self.player1} rolled str({self.Total})")
        print(f"{self.player2} rolled {self.Total}")
