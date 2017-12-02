nums = [-1, 5, 7, 1, -5]
x = nums[0]
x2 = 0
found = False
for i in range(1, len(nums)):
    if x + nums[i] ==0:
        x1 = nums[i]
        found = True
        break
if not found:
    print("Not found")
else:
    print("Found {0} and {1}".format(x, x1))
