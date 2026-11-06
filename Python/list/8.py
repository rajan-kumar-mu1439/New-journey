 # Reverse a list without using reverse() or slicing.

list = [1,2,3,4,5,6,7,8,9]
new_list = []

for i in list:
    new_list.insert(0,i)
print(new_list)

