import random

num = random.randint(1,100)

while True:
    user = int(input("Enter your number : "))

    if num > user:
        print("Greather than")

    elif num < user:
        print("Less then") 

    else:
        print( )
        print(" ---> Number find :", num)  
        print( )
        break     
