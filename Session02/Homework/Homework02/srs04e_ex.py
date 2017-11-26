m= int(input("Enter m:"))
n= int(input("Enter n:"))
for a in range(0, m):
    if a % 2 == 0:
        for b in range(1, n+1):
            if b % 2 == 0:
                print("*", end=' ')
            else:
                print("X", end=' ')
    else:
        for c in range(1, n+1):
            if c % 2 == 0:
                print("X", end=' ')
            else:
                print("*", end=' ')
    print()
