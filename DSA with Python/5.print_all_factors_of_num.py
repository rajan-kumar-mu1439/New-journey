num = 10
result = []
for i in range(1, num+1):
    if num % i == 0:
        result.append(i)
print("First method :",result)     


# second method

result1 = []
for i in range(1, num//2+1):
    if num % i == 0 : 
        result1.append(i)
result1.append(num)
print("Second method :", result1)        


# 3 method :- OPtimal solution

from math import sqrt
num1 = 36
result2 = []
for i in range(1, int(sqrt(num1))+1):
    if num1 % i == 0:
        result2.append(i)

        if num1//i !=i :
            result2.append(num1//i)
print("optimal solution : ",sorted(result2))        
