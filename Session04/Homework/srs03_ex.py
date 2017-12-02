n = False
while not n:
    try:
        a = int(input("Enter a number: "))
        n = True
    except ValueError:
        print("Not a number!")
if a == 2:
    print(a, "is a prime number!")
if a < 2:
    print(a, "is not a prime number!")
for i in range(2, a):
    if a % i == 0:
        print(a, "is not a prime number")
        break
    elif a == i + 1:
        print(a, "is a prime number")
