#  #  Count how many even and odd numbers are in a list.


list = [1,2,3,4,5,6,7,8,9]
# even = 0
# odd = 0

# for i in list:
#     if i%2 == 0:
#         even= even + 1
        
#     else:
#         odd= odd + 1  
        
# print("Even count :", even)        
# print("Odd count :", odd)        



even = sum(1 for i in list if i%2==0)
odd = len(list) - even
print("even count:", even)
print("Odd count :", odd)