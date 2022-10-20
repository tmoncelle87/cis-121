#write a function that creates a file with 300 random numbers from 1-2000
#my attempt
# import random

# def numbers():
#     list1=[]
#     for i in range(300):
#         list1.append(random.randint(1,2000))
#     with open("randomValues.txt",'w') as f:
#         for number in list1:
#             f.write(str(number)+'\n')
#             for number in list1:
#                 if number % 2 == 0:
#                     f.write(str(number)+("     even") +'\n')
#                 else:
#                     f.write(str(number)+("     odd") + '\n')
# print(numbers())

    
#create another functiom that tkes the file we created and adds the words (even or odd next to the numbers)


# dicti={}
# for number in numbers():
#     if str(number) in dicti:
#        pass
#     else:
#        dicti[str(number)] = dicti.count(number)
#Fix this one  below
# attempt this later
# write a function that have similar keys. return only one dictionary that has all all the values for a given key
# my attempt
# dicti1= {
#     "data": [0],
#     "info":"NA"
# }
# dicti2={
#     "data":[3],
#     "Stats":"NA",
#     "info": "NA"
# }
# dicti3={}
# def functiony(dicti1,dicti2):
#     for j in dicti1:
#         for b in dicti2:
#             if j ==b:
# def checkDictionary(data1,data2):
#     result ={}
#     for key in data1:
#         if key not in result:
#             result[key] = data1[key]
#         else:
#             result[key].append(data1[key])
#             for key in data2:
#                 if key not in result:
#                     result[key]=data2[key]
#                 else:
#                     result[key].append(data1[key])
#                     return result
# print(checkDictionary(data1,data2))
#to replace str.replace("what to replace","what to replace with")
#thursdayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
from car import Car
r32= Car(4,"RB25","GTR R32",1992)
r32.change_year(1993)
p_911=Car(4,"WW91","911",1993)
print(p_911)
from employee import Employee
tony=Employee(65,40,"Tony","dishwasher",0)
print(tony)
#create a class of employees should have hourly, position,name , hours a week.method that calulates yearly salarly
from circle import Circle
c1= Circle(70)
print(c1)