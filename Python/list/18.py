# Merge two sorted lists into one sorted list without calling sort().

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]


for i in list1:
    list2.append(i)

result =list( set(list2))
print(result)
    