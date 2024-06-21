# i=int(input("Enter a number"))
# while(i<=38):#Makes iput to loop till user does'nt write value greater than 38
#    i=int(input("Enter a number"))
#    print(i)
# print("End of loop")

# decrementing while Loop
ino=5
while ino>0:
    print(ino)
    ino-=1
else:
    print("Ended the loop has")   
print()
print()
print()
print()
print()
while True:
    try:
        age=int(input("Enter your age"))
        if age >18:
            print("You're eligible to get a driving lisence")
        if not age>18:
            print("You're not eligible for a driving lisence ")
        again=input("Do you wnat to check another age?")    
        if again!="yes":
         print("ok enjoy")
         break
    except ValueError:
      print("Enter a number")               

print()
print()
print()
print()

for l in range(0,12):
   if l==10:
    continue
   print(f'The multiples of 5 is :\n 5 *{l+1} {5 * l+1}')
               
#Do while in pyhton
while True:
   i=int(input("Enter a positive number : "))
   if i>0:
    print(f"The positive number is {i}")
   elif i<0:
      print("Enter a positive number")
      break
