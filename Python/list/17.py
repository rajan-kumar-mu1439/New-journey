# Find the maximum sum of a contiguous subarray (Kadane's algorithm).

list = [2, 1, -1, 3, -2, 1, 3, -2]
curr_num = list[0]
max_num = list[0]

for i in list[1:]:
    curr_num = max(i, curr_num + i)
    max_num = max(max_num, curr_num)

print(max_num)    

