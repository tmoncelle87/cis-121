# list1= [1,5,7,9,8,4]

# #first thing i did is create a function and a list.
# #after that my function checks if an item in my list is even or odd and then adds them to a dictionary
# def odd_even(list1):
#     dicti={
#     "even": 0,
#     "odd": 0
# }

#     for i in (list1):
#         if i % 2 == 0:
#             dicti["even"] = i
#         else:
#             dicti["odd"] = i
#     i+=1
#     return dicti
#     with open("file.txt", 'w') as f:
#         f.write(str(dicti))
# print(odd_even(list1)) 


# i have it mostly done but just cant remember how to add multiple things to a dictionary also when i try and create a new file inside of the function it is not working
#Generate two list with 200 random numbers from the ranges
#1-100 and then determine how many numbers generated are the same.
#Keep track of the amount of times each number appears in each list in
#a single dictionary.

# import random
# listi= []
# for i in range(200):
#     listi.append(str(random.randint(1,101)))
# temp = {}
# for number in listi:
#      if str(number) in temp:
#         pass
#      else:
#        temp[str(number)] = listi.count(number)

# print (temp)
#finished this one wooooooo!
#my test axiety was messing me up hard and made me forget this simple thing on how to track things in a dictionary
#first thing i did was open the file and create data to make it easier for me
#next i will be adding each number together in a month
file =("steps.txt",'r') 
data= file.read()
january=[]
febuary=[]
march=[]
april=[]
may=[]
june=[]
julya-[]
august=[]
september=[]
october=[]
november=[]
december=[]
#ik that this is horrible but i dont have enough time 

line = 0
while line in data < 31:
    january.append(line)
    line +=1
while line in data > 31 and line in data <59:
    febuary.append(line)
while line in data >  and line in data <:
    march.append(line)
while line in data >  and line in data <:
    april.append(line)
while line in data >  and line in data <:
    may.append(line)
while line in data >  and line in data <:
    june.append(line)
while line in data >  and line in data <:
    julya.append(line)
while line in data >  and line in data <:
    august.append(line)
while line in data > and line in data <:
    september.append(line)
while line in data >  and line in data <:
    october.append(line)
while line in data >  and line in data <:
    november.append(line)
while line in data >  and line in data <:
    december.append(line)
#what i am doing here is checking each month then appending it to a list after that i was going to calculate the average of each

