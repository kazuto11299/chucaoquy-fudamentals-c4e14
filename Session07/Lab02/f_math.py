from random import randint, choice
x = randint(1, 10)
y = randint(1, 10)
sum = x + y
sums = [x + y + 1, x + y - 1, x + y]
a = choice(sums)
print(int(x), "+", int(y), "=", a)
ans = str(input("(Y/N)? "))
if a == sum:
    if ans == "y":
        print("Nice!")
    elif ans == "n":
        print("Noob!")
else:
    if ans == "n":
        print("Nice!")
    if ans == "y":
        print("Noob!")
