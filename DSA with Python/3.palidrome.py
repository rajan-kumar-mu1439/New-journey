num=12321
original = num 
result = 0
while num >0:
    last_digit = num % 10
    result = result * 10 + last_digit
    num = num // 10

if(result == original):
    print("Palidrome")
else:
    print("not palidrome")    