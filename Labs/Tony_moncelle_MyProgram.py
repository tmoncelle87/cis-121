import Labs.Tony_Moncelle_Stats2 as Tony_Moncelle_Stats2
file= open("50DayFruitData.txt",'r')
#gathering all lines and seperating them by /n
data= file.read().splitlines()



data.pop(0)
apple_tracker=[]
banana_tracker =[]
strawberry_tracker= []
for item in data:
    temp=item.split()

    if temp[1] == "apple":
        apple_tracker.append(int(temp[2]))
    elif temp[1] == "banana":
        banana_tracker.append(int(temp[2]))
    elif temp[1]== "strawberry":
        strawberry_tracker.append(int(temp[2]))
            

# strawberry_mean= Tony_Moncelle_Stats2.mean(strawberry_tracker)
# strawberry_median= Tony_Moncelle_Stats2.median(strawberry_tracker)
apple_mean= Tony_Moncelle_Stats2.mean(apple_tracker)
apple_median= Tony_Moncelle_Stats2.median(apple_tracker)
apple_mode= Tony_Moncelle_Stats2.mode(apple_tracker)

dictionary={
    "apple_means" : [apple_mean],
    "apple_median" : [apple_median],
    "apple_mode" : [apple_mode]
}
print("the mean of apples eaten", apple_mean)
print("the median of apples eaten", apple_median)
print("the mode of apples eaten is (are)",apple_mode)

# print("the mean number of banas", banana_mean)
# print("the median number of bananas", banana_median)
with open("results.txt",'w') as f:
    f.write("the mean number of apples eatan are: "+ str(dictionary["apple_means"]) + "\n" +"the median number of apples eaten are: "+ str(dictionary["apple_median"]) + "\n" +"the mode number of apples is (are): "+ str(dictionary["apple_mode"]) + "\n")
    # f.write("the mean number of bananas eaten are: "+str(banana_mean)+ "\n" +"the median number of bananas eaten are: "+ str(banana_median) + "\n")
    # f.write("the mean number strawberries eaten are: "+str(strawberry_mean)+ "\n" +"the median number of strawberries eaten are:" + str(strawberry_median) + "\n")