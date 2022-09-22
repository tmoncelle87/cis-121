from decimal import DivisionByZero
from turtle import done

#made the question for user
user_number = int(input("Please enter a upper bound for check!"))
#trying to make it so my first loop goes from 1 to number user entered
abundant_number= 0
perfect_number = 0
deficient_number = 0
Divisor = 0
test = 1 

summ = 0
while test <= user_number :
# now I finished that and will be trying to get my divisors I have no clue how to start but once I do i=I think it will be not that bad
    while test >= Divisor :
        if Divisor % test == 0:
            summ+= test
        test += 1
        # now That I have that sorted I will be finding how many divisors and abundant numbers and perfect number there are
            if summ > user_number :
                