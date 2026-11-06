num = [1,1,2,2,3,3,4,4,5,5,6,6,6]
dict = dict()
for i in range(0, len(num)):
    if num[i] in dict:
        dict[num[i]] +=1
    else:
        dict[num[i]] = 1   
print(dict)        