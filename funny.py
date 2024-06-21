def mult(badmas):
 for k in range(1,11):
  print(f"{badmas} *{k} = {badmas * k}")
num=int(input('Enter a number : '))
mult(num)

#Fun to find gmean
def gmean(a,b):
   mean=(a*b)/(a+b)
   return mean
c=4
d=2
print(gmean(c,d))

#Function arguments
def avg(a,b=0):#Default argument is giving default value
  sup=(a+b)/2
  return print(f"The avg of {a} and {b} is {sup}")
  
print(avg(a=2))#Keyword argument this is as we have used a=2 i.e order dont' matter
#Again a is "required argument" because a is not given a default argument

#Arbitary Arguments
def average(*nums):
   print(type(nums))
   sum=0
   for i in nums:
     sum+=i
   # print(f"Average no is {sum/len(nums)} ")
   return sum/len(nums)
c=average(5,6,7,1)
print(c)

def wsup(*names):
  for name in names:
   print("Hello",name,endswith=",")
wsup("bobby","Lobby","Robby")

# def name(*name):
#   print('Hey, ',name[0],name[1],name[2])
# name("bobby","Lobby","Robby")