#EXAMPLES
'''
print("welcome to sagar hotel:")
print("1.dosa\n","2.idli\n","3.poori\n","4.chapathi\n","5.tea\n","6.coffee\n")
option=int(input("enter your choice:"))
if option==1 or option==2:
    print("Go to counter A")
elif option==3 or option==4:
    print("GO to counter B")
elif option==5 or option==6:
    print("Go to counter C")
else:
    print("you are not ordered")
'''
#example 2

print("welcome to sagar hotel:")
print("1.dosa\n2.idli\n3.poori\n4.chapathi\n5.tea\n6.coffee")
option=int(input("enter your choice:"))   
match option:
    case 1:
        print("go to counter A")
    case 2:
        print("go to counter A")
    case 3:
        print("go to counter B")
    case 4:
        print("go to counter B")
    case 5:
        print("go to counter C")
    case 6:
        print("go to counter C")
    case _:
        print("no order to process")

# print mo\nkey"s cafe (number 1)
# escape characters
'''
print("1:\tdosa\n2:\tidli\n")
'''     
