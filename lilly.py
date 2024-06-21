colour=["Crimson Red","Violet","Black","Purple"]
print(colour[-2])
print(colour)
if "Crimson Red" in colour:
    print("this colour ,'tis present in the colour list")
else:
    print("No it's not present")
# ?list comprehension    
print()
print()
print()
print()
print()
lst=[i*i for i in range(10) ]
print(lst)
lst=[i*i for i in range(10) if i%2==0 ]
print(lst)


#list methods
l=[1,2,41,33,4,5,6,65]
#adding an element at .last
l.append(8)
l.append(3)
print(l)
#Sort 

l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.sort(reverse=False)
print(l)
print()

l.reverse
print(l)
print()
print()
print(l.index(2))
