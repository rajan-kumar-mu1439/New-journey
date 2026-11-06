# Find all pairs in a list whose sum equals a target value.

a = [1,2,3,4,5]
target = 15
add = 0

for i in a:
    add = add + i
if(target == add):
    print("Yes")
else:
    print("No")        