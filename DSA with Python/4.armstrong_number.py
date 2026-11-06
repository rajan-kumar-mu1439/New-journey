num = 3709
original = num 
total = 0
count = len(str(num))

while num > 0:
    last_digit = num % 10
    total = total + (last_digit ** count)
    num = num // 10

if original == total:
    print("Armstrong")
else:
    print("Not Armstrong")    