from random import *
import random
nums = [-22, -1, 33, 34, 69, 78]
n = choice(nums)
num = input("Guess my chosen number? ")
lo = 0
hi = len(nums)
guess = False
while not guess:
    mid = (lo + hi)//2
    num = nums[mid]
    if num == n:
        guess = True
        print("Congratulations!")
        break
    elif n < num:
        hi = mid
        print("Unlucky! The number is in the left side")
    else:
        lo = mid + 1
        print("Unlucky! The number is in the right side")
