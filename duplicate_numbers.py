# Get Input as String
a = input()  # '9,10,2,3,3,4,5,6,7,8,1'
# Split input by comma and store in num array or list
num = a.split(',')  # ['9','10','2','3','3','4','5','6','7','8','1']

# Convert (Cast) string to integer
for i in range(len(num)):
    num[i] = int(num[i])
# [9,10, 2,3,3,4,5,6,7,8,1]
# Sorting
num.sort()  # [1,2,3,3,4,5,6,7,8,9,10]

# Duplicate code logic
duplicate = -1
for i in range(1, len(num)):
    if num[i] == num[i - 1]:
        duplicate = num[i]
        break  # only one in problem statement
print(duplicate)
