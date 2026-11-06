name = input("Enter Your name: ")
budget = input("Enter your monthly budget: ")

n = 1
while n < 10:
    expend = input("Enter expense name: ")
    amount = input("Enter amount: ")

    i = 1
    while i < 10:
        print("===== EXPENSE REPORT =====")
        print("Name: ", name)
        print("Budget: ",budget)
        
        dict = {
            expend : amount
        }
        print(dict)

    
