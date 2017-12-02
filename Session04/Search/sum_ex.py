num = [-4, 33, 0, 69, 34, -78]
# print("Here are our numbers:", *num, sep = ", ")
# print(sum(num))
# print(min(num))
minimum = num[0]
for nums in num:
    if minimum > nums:
        minimum = nums
print("Min: ", minimum)
