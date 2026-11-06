num = 54899
# count = 0
# while num > 0:
#     count+=1
#     num = num//10
# print(count)


# Method 2.
from math import *
def countDigit(num):
    return int(log10(num)+1)

print(countDigit(num))