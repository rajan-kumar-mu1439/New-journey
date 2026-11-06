# Move all zeros to the end while preserving the order of other elements.


a = [2,4,5,7,0,4,2,0,5,1,0,9,8]
non_zero = []
zero = []

for i in a:
    if i == 0:
        zero.append(i)
    else:
        non_zero.append(i) 

result = non_zero + zero
print(result)