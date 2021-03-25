# Find the maximum and minimum element in an array
arr = [1000, 11, 999999, 445, 1, -1, 330, 3000]

min = None
max = None

# first compare the first two elements
if arr[0] > arr[1]:
    max = arr[0]
    min = arr[1]
else:
    min = arr[1]
    max = arr[0]

# assign the max and min value, use theese as refrence/ flag and compare the rest of the array
for i in range(2, len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print("The element in the array is {} and the min element in the array is {} ".format(max, min))
