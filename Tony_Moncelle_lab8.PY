def cleandata(data):
    filename= open("randomValues.txt",'r')
    temp = []
    for i in data:
        if i.isdigit() :
            temp.append(int(i))
    return temp
def readfile(filename):
    file= open("randomValues.txt",'r')
    temp = file.read().splitlines()
    temp=cleandata(temp)
    return temp
data=readfile("randomValues.txt")
print(data)

def findMin(index,current_min,data):
    if len(data) == 0:
        print("empty list no work")
    if len(data) == 1:
        return data[0]

    min = data[index]

    if min <= current_min:
        current_min= min

    if index >= len(data)-1:
        return current_min
    elif index <= len(data) - 1:
        return findMin(index+1,current_min,data)


print(findMin(0,data[0],data))
def findMax(index,current_Max,data):
    if len(data) == 0:
        print("empty list no work")
    if len(data) == 1:
        return data[0]

    max = data[index]

    if max >= current_Max:
        current_Max= max

    if index >= len(data)-1:
        return current_Max
    elif index <= len(data) - 1:
        return findMax(index+1,current_Max,data)


print(findMax(0,data[0],data))
def extrema(data,calculate_min=True,calculate_max=True):
    if calculate_min == True and calculate_max == True:
        return [findMin(0,data[0],data),findMax(0,data[0],data)]
    elif calculate_min== False: 
        return [findMax(0,data[0],data)]
    elif calculate_max == False:
        return [findMin(0,data[0],data)]

print(findMin(0,data[0],data))
print(findMax(0,data[0],data))
print(extrema(data))
print(extrema(data,False))
print(extrema(data,False,False))
print(extrema(data,calculate_max=False))

