# Rotate a list to the right by k positions.

list = [1,2,3,4,5]
k = 2

k = k % len(list)

result = list[-k:] + list[:-k]
print(result)
