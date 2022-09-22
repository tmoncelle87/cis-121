#a this one does not work because there it thinks of the input as a string and not a int so what they need to do is to have it be age = int(input("please enter your age: ")

#b this one does not work because number is not defined 

#c does work 

#d does not work because print is not indented or "tabbed"

#e does not work because there is no true statement or false statement to stop the while loop




# milk = int(input("hello customer how much milk would you like to purchase?"))

# eggs = int(input("hello customer how many eggs would you like to purchase?"))
# #now I am adding all of my questions for the user to determine what they are buying
# bacon = int(input("hello customer how much bacon would you like to purchase?"))
# #now I am making an equation to find the total cost of the users groceries
# total_cost = (milk * 2) + (eggs * 1.5) + (bacon * 3)
# tax= .11
# #I know this could be done simply but not sure how yet but this is how I calculated the total cost with tax
# tax_total_cost = total_cost +total_cost * tax
# print("the total cost of your groceries is $", tax_total_cost)
# #this prints of the total cost for the customers goods

# #fisrt I had a question that asks for a phone number
# phone= (input("please enter your phone digits"))
# #next this took me a long time but I eventually figured it out but I was trying to print the number the user given in phone number form by string manipulation
# print("("+ (phone[0:3]) + ")" ,(phone[3:6]) ,"-", (phone[6:10]))


#next I will be trying to create a loop that finds if a number is a divisor of 48
#not sure how to find that but im guessing that it should be if 48 / number == int : 
#first i defined number as 0
number = 0
#now i am unsure how to make the numbers in range get divided automatically
#What I am doing now is troubleshooting trying to find the correct way to do this
while number in range(2,61):
    number = 0
    if 48 / number == int:
        print(number)
