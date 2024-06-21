 #Add , subtract and divide and multiply 
try:           
      a=input('Enter a number:\n')
      b=input('Enter another number:\n')
      a=int(a)
      b=int(b)
except ValueError:
    print("Please enter a valid number")      
     #Addition
print(f"The sum of {a} and {b} is {a +b}")
     #Diff
print(f"The diff bewtween  {a} and {b} is {a - b}")
     #Muliply
print(f"The product of {a} and {b} is {a * b}")
     # division
print(f"The division of {a} and {b} is {a/b}")

#Driving Age
age=input("Enter you age\n")
age=int(age)
if age<18:
     print("Sorry you're not able to get a lisence due to your age")
else:
     print("You can have a driving lisence")     


#next
num=input("Enter a number:\n")
num=int(num)
if num <0:
     print("The number you've provided is negative")
elif num==0:
     print("The number you've provided is perfectly zero ") 
else:
    print("Thou the lords of the thousand seas, have invoked a positive number ")         