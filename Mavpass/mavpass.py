#ask user waht favorite color is if blue then say you like blue if red say disqusting 
# color = input("what is your favorite color?")
# if color == "blue" :
#     print("you like blue")
# elif color == "red" :
#     print("that's disqusting")
# else :
#     print("That's okay")
# even = 0
# while even < 10 :
#     random_number = int(input("please enter a random number"))
#     if random_number == 40 or random_number == 10 :
#         print("words")
#     if random_number % 2 == 0:
#         even =+1
#         print(random_number)
#         print(even)

   
# cost= float(input("enter cost of clothing: "))
# tax= .09
# discounted= (cost *.7)
# total_cost = (discounted * tax) + discounted
# print("$",total_cost)

# pool_height= float(input("Hey Ye what is the height of hot tub in inches?"))
# pool_length= float(input("Hey Ye what is the length of hot tub in inches?"))
# pool_width= float(input("Hey Ye what is the width of hot tub in inches?"))
# cubic_inches = (pool_height * pool_length * pool_width)
# gallons = cubic_inches / 231
# print("Ye we have" , gallons , "gallons of water")


# def function():
#     count = 0 
#     total = int(input("what are we counting towards?"))
#     while count < total :
#         print(count)
#         count +=1

# def function2():
#     function()
#     print("done")
# function2()
# parameter_= int(input("enter a number to find the true divisors"))

# def     function(parameter_):

#     positive_even_divisor =[]
#     for i in range(1,parameter_):
#         if i % 2 == 0 and parameter_ % i == 0:
#             positive_even_divisor.append(i)
#     print(positive_even_divisor)
# function(parameter_)
# birthday= input("what month is your birthday")
# months= ["january"........]
# temp = []
# for i in months:
#     if i == birthday :
#         temp.append([i,"yes"])
#         else:
#             temp.append([i,"no"])

# print(temp)

# def function():
#     custumer_id=int(input("what is the customers id: "))
#     import random
#     dicti= {}
#     for i in range(1,201):
#         dicti[i] = random.randint(1,101)
#     dicti.pop(custumer_id)
#     with open("palindromes.txt",'w') as f:
#         f.write(str(dicti))
# function()    
# import random    
# list=[]
# dicti= {}
# for i in range(1,201):
#     list.append(random.randint(1,201))
# print(list)
# for i in range(0,199):
#     if i == 0:
#         dicti[list[i]] = list[i+1]
#     if i % 2 == 0:
#         dicti[list[i+1]] = list[i]
# print(dicti)
from string import capwords


class hand:
    def __init__(self,card,wins):
        self.wins=wins
    def find_winner(self,wins,list):
        while wins <= 6:
            if player1.cardone_suite == player2.cardone_suite: 
                if player1.cardone_value > playe2.cardone_suite:
                    player1.win +=1
                    wins +=1
                    return player1.win and wins
            else:
                player2.win +=1
                wins +=1
                return  wins and playr2win
