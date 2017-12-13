from random import randint, choice
x = randint(1, 10)
y = randint(1, 10)
sum = x + y
sums = [x + y + 1, x + y - 1, x + y]
a = choice(sums)
multi = x * y
multis = [x * y + 1, x * y - 1, multi]
b = choice(multis)
divide = x / y
divides = [x / y + 1, x / y - 1, divide]
c = choice(divides)
minus = x - y
minuss = [minus - 1, minus + 1, minus]
d = choice(minuss)
n = [(int(x), "+", int(y), "=", a), (int(x), "-", int(y), "=", d), (int(x), "*", int(y), "=", b), (int(x), "/", int(y), "=", c)]
m = choice(n)
print(*m)
ans = str(input("(Y/N)? "))
if m == n[0]:
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
if m == n[1]:
    if d == minus:
        if ans == "y":
            print("Nice!")
        elif ans == "n":
            print("Noob!")
    else:
        if ans == "n":
            print("Nice!")
        if ans == "y":
            print("Noob!")
if m == n[2]:
    if b == multi:
        if ans == "y":
            print("Nice!")
        elif ans == "n":
            print("Noob!")
    else:
        if ans == "n":
            print("Nice!")
        if ans == "y":
            print("Noob!")
if m == n[3]:
    if c == divide:
        if ans == "y":
            print("Nice!")
        elif ans == "n":
            print("Noob!")
    else:
        if ans == "n":
            print("Nice!")
        if ans == "y":
            print("Noob!")
