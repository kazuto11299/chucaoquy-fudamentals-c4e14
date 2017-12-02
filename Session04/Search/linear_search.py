num = [69, 99, 33, 34]
n = int(input("Enter a number: "))
found = False
found_i = - 1
# find_first, find_one
# find_all
for i, nums in enumerate(num):
    if n == nums:
        found_i = i
        found = True
        break
if not found:
    print("Not found")
else:
    print("Found {0} at index {1}".format(n, found_i))
