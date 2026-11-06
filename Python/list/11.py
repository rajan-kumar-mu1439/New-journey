# Find the second-largest distinct number in a list without using sort().

a = [2,5,7,8,9,2,3,5,1,7,10,10]
b = list(dict.fromkeys(a))
large = max(b)
b.remove(large)
second_large = max(b)
print(second_large)
