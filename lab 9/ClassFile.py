class RoboFriend:
    def __init__(self,Name_,Age_):
        self.Name_ = Name_
        self.Age_= Age_
    def stateName(self):
        print(f"Hello. My name is: {self.Name_}")
        return ""
    def stateAge(self):
        print(f"I'm: {self.Age_} Years old")
        return ""


