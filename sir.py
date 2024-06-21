# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a
# try:
#     time=int(input("Enter a time (0-24) : "))
#     if 0<=time<12:
#         print("Good morning bro")
#     elif 12<=time<17:
#         print("Goof evening bro")
#     elif 17<=time<20:
#         print("Good evening bro")
#     elif 8<=time<=24:
#         print("Good night bro") 
#     else:
#       print("Congrats on living in a different dimension")
# except ValueError:
#     print("WOW! you're so different aren't you?")     

import time
timestamp=time.strftime('%H:%M:%S')
timestamp1=time.strftime('%H')
timestamp2=time.strftime('%M')
timestamp3=time.strftime('%S')
timestamp1=int(timestamp1)
print(timestamp)
if 0<=timestamp1<12:
   print("Good morning bro")
elif 12<=timestamp1<17:
            print("Good afternoon bro")
elif 17<=timestamp1<20:
            print("Good evening bro")
elif 20<=timestamp1<=23:
            print("Good night bro") 
else:
          print("Congrats on living in a different dimension")