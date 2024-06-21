x=int(input("Enter the value of x : "))
match x:
    case 0:
        print("X is zero")
    case 14:
        print("X is fourteen")
    case _ if x !=90:
        print(f"The value you've entered is not equal to 90")
    case _ if x !=98:
        print(f"The value you've entered is mot equal to 98")
    case _ :
        print(f"The value you've entered is {x}")
