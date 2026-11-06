# Flatten a nested list one level deep, such as [[1, 2], [3, 4]] into [1, 2, 3, 4].


l= [[1, 2], [3, 4]]
result = []
for i in l:
    for j in i:
        result.append(j)
print(result)        