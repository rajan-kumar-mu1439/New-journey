# Find the element that appears more than n/2 times, if one exists.

numbers = [2, 2, 1, 2, 3, 2, 2, 2]

length = len(numbers)

for num in numbers:
    count = numbers.count(num)

if count > length / 2:
    print(num)
else:
    print("Not")