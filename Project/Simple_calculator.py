while True:  
    num_1 = int(input("Enter your number: "))
    num_2 = int(input("Enter your number: "))

    print ("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Choice your action :"))

    if choice == 1:
        print("Addition: ", num_1 + num_2)

    elif choice == 2 :
        print("Subtraction :", num_1 - num_2)

    elif choice == 3:
        print("Multiplication :",num_1 * num_2)

    elif choice == 4:
        if num_2 == 0 :
            print("Can not divided by 0.")
        else :
            print("Division :", num_1 / num_2)    

    else:
        print("Invalid Choice")

