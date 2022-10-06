import Tony_Moncelle_Stats
file= open("500DayFruitData.txt",'r')
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
            

strawberry_mean= Tony_Moncelle_Stats.mean(strawberry_tracker)
strawberry_median= Tony_Moncelle_Stats.median(strawberry_tracker)
apple_mean= Tony_Moncelle_Stats.mean(apple_tracker)
apple_median= Tony_Moncelle_Stats.median(apple_tracker)
banana_mean= Tony_Moncelle_Stats.mean(banana_tracker)
banana_median= Tony_Moncelle_Stats.median(banana_tracker)
print("the mean of apples eaten", apple_mean)
print("the median of apples eaten", apple_median)
print("the mean number of banas", banana_mean)
print("the median number of bananas", banana_median)
with open("Tony_moncelle.txt",'w') as f:
    f.write("the mean number of apples eatan are: "+ str(apple_mean) + "\n" +"the median number of apples eaten are: "+ str(apple_median) + "\n")
    f.write("the mean number of bananas eaten are: "+str(banana_mean)+ "\n" +"the median number of bananas eaten are: "+ str(banana_median) + "\n")
    f.write("the mean number strawberries eaten are: "+str(strawberry_mean)+ "\n" +"the median number of strawberries eaten are:" + str(strawberry_median) + "\n")