
#create a function taht takes two lists and makes them into a dictionary
#my try
# dictionary= {}
# list_1 = [1,2,3]
# list_2 =["number 1", "number 2", "number 3"]
# def combine_list():
#     for i in list_1:
#         dictionary.append(list_1)
#         return dictionary
# combine_list()
# print(dictionary)






# # # def create_dictionary(keys,data):
# # #     temp= {}
# # #     if len(data) == len(keys):
# # #         for i in range(len(keys)):
# # #             temp[keys[i]] = data[i]
# # #     return temp
    

# # # list1= ["num 1", "num 2"]
# # # list2= [1,2]
# # # print(create_dictionary(list1,list2))

# # #create a function that can multiply all numbers in a dictionary by a given nmber
# # info = {
# #     "num 1" : "12",
# #     "num 2" : "abcs",
# #     "num 3" : "56"
# # }
# # #my try
# # # def multiply_dictionaries(keys,data):
# # #     for i in info:
# # #         if i.isdigit
# # #         i = data
# # info["num 1"]
# # def multiplyvalues(data,number):
# #     for key in data:
# #         if data[key].isdigit():
# #             print(data[key],number,int(data[key])*number)

# # multiplyvalues(info,2)

# import random
# #create a function that generates a dictionary with 5 numbers. then make another funciton that generates random numbers until it generates one inside of the dictionary
# #my attempt
# # def random_number(key,data):
# #     dicti = {}
   
# #     for i in range(0,5):
# #         dicti["number"] = 1

# def createdictionary():
#     temp = {}
#     for i in range (5):
#         temp["number " +str(i+1)] = i * 2

#     return temp
# x = createdictionary()

# def guessNumber(data):
#     guess= False
#     values= getData(data) 
#     while guess != True:
#         random_number = random.randint(1,1000)
#         if random_number in values:
#             print("found one! ", random_number)
#             guess = True


# def getData(data):
#     temp = []     
#     for i in data :
#         temp.append(data[i])
#     return temp
# print(x)
# guessNumber(x)

#practice using dicionaries and lists as ell as read a file and writing a file

#all the probelms given today are on the same level of the exam
#nned to know how to add things to 

#write a function that creates two lists of random values. the user should send as a parameter how many elements the list shoudl have
#my try
# parameter_=int(input("enter a parameter: "))
# list_1=[]
# list_2= []
# import random
# print(parameter_)
# def list(parameter_): 
#     while i < parameter_ :
#         list_1.rand.append
#correct #
# import random
# def creatlist(amount):
#     list1=[]
#     list2=[]
#     for i in range(amount):
#         list1.append(random.randint(1,100))
#         list2.append(random.randint(1,100))

#     return [list1,list2]
# print(creatlist(5))

#write a function that can find how many times the letter a and u can be found make that into a dictionary
#my try with a little help works
# def findamount(word):
#     dicti={
#         "a": 0,
#         "u": 0,
#     }

#     for letter in word:
#         if letter == "a":
#             dicti["a"] +=1
#         elif letter == "u":
#             dicti["u"] +=1
#     return dicti 

# print(findamount("universe"))

#write a function that can ask for 10 best run times then calculate the average and check what the best times and worst times
#my try

# def findtimes():
#     times = []

#     for i in range(10):
#         ten_run_times= float(input("enter 10 best 4 mile run times"))
#         print(ten_run_times)
#         times.append(ten_run_times)

# def runnerinfo():
#     times= []
#     info= {
#         "times": [],
#         "avg": 0,
#         "best time": 0,
#         "worst time": 0,
#     }
  
#     import statistics
#     for i in range(10):
#         user= int(input("please enter a time"))
#         info["times"].append(user)
#         if user > info["worst time"]:
#             info["worst time"] = user
#         if user < info["best time"] or info["best time"] == 0 :
#             info["best time"] = user

#     info["avg"] = statistics.mean(info["times"])
#     return info
# print(runnerinfo())

#write a function that can take two list and generate a dictionarys 
#then multiply all the values by 5
#my attempt
# def multiply():
#     list1= [1,2,3]
#     list2= ["num 1","num 2", "num 3"]
#     dicti={

#     }
#     for value in list:
#         for i in range(len(list2)):
#             dicti[list] = 



def creatdic(list1,list2):
    info={}
    for i in range(len(list1)):
        info[list1[i]] = list2[i]

        info["Num "+str(list2[i] *5)] = list2[i]*5
    return info
print(creatdic(["num 1","num 2", "num 3"],[1,2,3]))