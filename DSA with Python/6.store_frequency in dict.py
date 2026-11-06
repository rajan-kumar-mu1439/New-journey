"""
Hashing Basics
:- Store the frequency of every element in a dictionary

"""

num = [5,3,1,6,5,3,2,1,2,6,3,5,1,6,2,1,1,1,3,3,5,6]
freq_map = dict()
for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]] = 1   

print(freq_map)



# 2.method
hash_map = dict()
for i in range (0, len(num)):
    hash_map[num[i]] = hash_map.get(num[i],0)+1
print(hash_map)    