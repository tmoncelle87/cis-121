#conditionals
# name="tony"
#number=10
# if number > 10 : 
#     print("this number is goated")
#     print("this is cool")
# elif number < 10 :
#     print("this number is less than 10")
# elif number == 10 :
#     print("this number is 10")
# elif number == 10 :
#     print("this number is 10")
# print("this isnt that bad")

# #create script that asks user for income
# income = int(45000)
# print("what is your income?")
# if income > 450000 :
#     print("damn you are rich you make", income, "$ each year")
# elif income < 450000 : 
#     print("you got it keep grinding champ you make", income,"a year")
# #works great
# number = 7
# while number < 10 : number == 50
#     print(number)
#     number = number + 1
#create guessing game give user 3 tries to guess right number




# win = 0
# chances = 0
# num = 4
# while chances < 3 and win != 1:
#     user = int(input("guess the number"))
#     if user == num :
#         print("yay")
#         win = 1
#     else :
#         chances += 1


#loat is distance = 1.23
#integer = number = 3

#write small script that asks user for number between 35 and 10000 when user enters number your program should print the numbers from that x number to 100 but if number is over 100 print 100 by itself
#did that then now have to make sure its an even number

# number = int(input("guess a even number between 35 and 1000?"))
# if 35 <= number <= 1000:
#     if number >= 100 :
#         print(100)
#     else :
#         while number <= 100 :
#             if number % 2 == 0 : finds even number 
#                 print(number)
#             number+=1
# else :
# #     print("you didn't listen")

# # #boolean
# # #winner = True
# # #loser = False

# #write a script that keeps asking user for number and check if number is even or odd. let user know what it is if they enter 0 stop asking
# # done = False
# # while done !=True :
# #     number = int(input("please enter a number.."))
# #     if number == 0 :
# #         print("bye")
# #         done = True
# #     elif number % 2 == 0 :
# #         print("this is even number")
# #     else:
# #         print("this is an odd number")
    
# #create script that asks user for name and income. let user know how much money they would have if they dont spend any money in 20 years
# # hey name, you make income a year!
# #this is how much money you would have in 20 years
# #40000 year 1
# #80000 year 2
# name = input("please enter your name")
# income = int(input("please enter your income"))

# print("hey",name, "you make", income, "a year")
# print("this is how much money you would have in 20 years")

# done = False
# years = 1
# money =0

# while done != True :
#     money = income*years
#     print("$"+str(money),"year",years)
#     years +=1
#     if money > 10000:
#         done = True
# even =+1 or even = even =+1
# for number in range(1,11) :
#     #only goes until a number less than the final number
#     print(number)


# for number in range(1,11):
#     if number % 2 == 0:
#         print(number)

# def askUserForName():
#     name = input("please enter your name:")
#     return name
# name = askUserForName()
# print(name)
#can have multiple variables with same names as long as it is not inside of the function or loop

# age=int(input("please enter your age"))
# for age in range(age,age + 21):
#     print(age)
# #first one i have done ever

# name = "tony"

# # # string manipulation
# # print(name[0:3])
# for letter in name:
#     print(letter)

# names = ["kendrick","grabriel"]
# randomstuff = [7,"ken",False,[],7.356]
# print(names[-1])
# for value in randomstuff :
#     print(value)
#create script that goes through list [2,45,32,43,22] and display every square of each number
from audioop import avg
from cmath import sqrt
from distutils.log import info
from multiprocessing.sharedctypes import Value
from tempfile import tempdir
from unittest import result


# list = [2,45,32,32,43,22]
# for num in list:
#     print(num**2,end="")
#create script that asks user for name age and number then add those values to a list and display them
# name= (input("enter name"))
# age= int(input("enter age"))
# number= int(input("enter number"))

# info = [name,age,number]
# print("name: ", info[0])
# print("age: ", info[2])
# print("number: ", info[2])

#create script that creates list without number 20 in it from this list 
# numbers = [20,34,23,2,11,24,4,20,21,12,20,20,20]
# clean = []

# for number in numbers:
# #     if number !=20:
# #         clean.append(number)
# # print(numbers)
# # print(clean)
# #my try
# # list1=["i","your","dude"]
# # list2=["am","boss","."]
# # for str in list1 and list2:
# #     print(list1[0] ,list2[0]  ,list1[1]  ,list2[1]   ,list1[2]  +list2[2])
# # #correct
# # list1=["i","your","dude"]
# # list2=["am","boss","."]
# # for word_index in range (0,3) :
# #     print(list1[word_index],list2[word_index], end =" ")

# # def function ():
# #     numbers= 0
# #     while numbers <= 10:
# #         user = (input("enter 10 numbers: "))
# #         user.isdigit()
# #         numbers += 1
# #     if numbers <= 5 :
# #         numbers += 1
# #         list1 = user
# #         print(list1)
# #         if numbers >= 5 :
# #             list2= user
# #             print(list2)
# #         else :
# #             print("done")
# # function()
# ###Today a new data type!
# names = ["Kendrick", 2, 3, .45, 23]
# #dictionaries
# #a data type that we can store data by key
# #to access data for names, example .45
# print(names[2])

# #to define an empty dictionary
# info_empty = {}
# #define a dictionary
# info = {
#     "Patient 0": ["Kendrick", "Morales", 23],
#     "Patient 1": 23,
#     "Patient 2": ["Bob", "Builder", 134]
# }

# #how to add values to dictionary
# info["Patient 3"] = ["Roger", "NA", "NA"]

# #print(info)

# print(info["Patient 3"])

# #-----------------------------------------------------------------------------------------------------------------------------------

# #CREATE A SCRIPT THAT ASKS THE USER FOR THEIR NAME, LAST NAME, AND AGE. KEEP THIS INFO STORED IN A DICTIONARY, THEN PRINT VALUES

# user_info = {
#     "user1": [input("What is your first name?: "), input("What is your last name?: "), input("What is your age?: ")]
# }

# print("Your name is", user_info["user1"[0]], user_info["user1"[1]], "you are", user_info["user1"[2]], "years old")

# #-----------------------------------------------------------------------------------------------------------------------------------
# #Create a script that ask the iuser for 5 soccer players and how many goals they made this season.
# #Calculate the average in a seperate function.


# def avg_goals(players):
#     sum = 0
#     for player in players:
#         sum += players[player]
#     return sum/len(players)

# players = {}

# for i in range(5):
#     name = input("Please enter players name: ")
#     goals = int(input("Please enter how many goals they scored this seaseon: "))

# players[name] = goals

# print("The average goals was:", avg_goals(players))

# #-----------------------------------------------------------------------------------------------------------------------------------
# #CREATE A FUNCTION THAT VERIFIES IF A KEY ALREADY EXISTS IN YOUR DICTIONARY

# dictionary1 = {
#     "Info_1": ["Ray", "Deml", 21],
#     "Info_2": ["Yar", "Lmed", 12]
# }

# def key_check(dictionary, key):
#     for key_value in dictionary:
#         if key_value == key:
#             return True
#     return False

# print(key_check(dictionary1, input("What key are you checking: ")))

# #-----------------------------------------------------------------------------------------------------------------------------------

# info1= {
#     "data": [1, 2, 3, 4, 5]
# }
# info2= {
#     "data": [6, 7, 8, 9, 10]
# }

# def add_together(data, data2):
#     total = []
#     for i in range(len(data["data"])):
#         total.append(data["data"][i] + data2["data"][i])
#     print(total)

# add_together(info1, info2)








# import random

# def str_to_int(data):
#   temp = []
  
#   for number in data:
#     if number.isdigit():
#       temp.append(int(number))    

#   return temp

# def add_5(data):
#   temp = []
#   for number in data:
#     temp.append(number+5)

#   return temp

# def write_to_file(data,name):
#   with open(name+".txt","w") as f:
#     for number in data:
#       f.write(str(number) +"\n")


  
# names = ["Kendrick","Morales"]

# info = {
#   "Kendrick": 23,
#   "Bob": 3456
# }


# #Open a file
# file = open("data.txt",'r')
# #Get data from file, remeber everything from a file is a consider a str
# data = file.read().splitlines()

# print(data)

# #Create a function that takes a list of values in str and returns a new list with only int.

# data = str_to_int(data)
# print(data)


# #Create a function that takes the numbers and adds 5 to them. 
# data = add_5(data)

# print(data)


# #Write the results to a new file

# with open("results.txt","w") as f:
#   for number in data:
#     f.write(str(number) +"\n")


# #Generate a random number
# a = random.randint(1,100)

# #Part 1
# #Generate a list with 100 random values. Then write the values to a file called "random_numbers_generated.txt"

# rand = []

# for i in range(100):
#   rand.append(random.randint(1,100))
  
# #writing to a file
# write_to_file(rand,"random_numbers_generated")



# #USE THE DOCS
# #Part 2
# #Create a function that counts how many times each number appears. Use a dict to keep track of it. 
# def count_num(data):

#   temp = {}

#   for number in data:
#     if str(number) in temp:
#       pass
#     else:
#       temp[str(number)] = data.count(number)

#   return temp


# c = count_num(rand)


# #Part C
# #Write the info from dict to a file called final.txt


# with open("final.txt",'w') as f:
#   for key in c:
#     f.write(key+": "+str(c[key])+'\n')
