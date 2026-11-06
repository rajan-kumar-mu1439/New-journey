n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,6,3,2]

dict = dict()
for i in range(0, len(n)):
    if m[i] == len(n):
        dict[n[i]] +=1
    else:
        dict[n[i]] = 1
print(dict)           