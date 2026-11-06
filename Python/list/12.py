# Find the common elements between two lists.

a = [1,2,3,4,5,6,10,7,8,4,3,6]
b = [1,2,3,9,4,5,6,6,7,8]
result = []

for i in a :
    if i not in b and i not in result:
        result.append(i)
for i in b:
    if i not in a and i not in result:
        result.append(i)   
print(result)