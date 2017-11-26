n = int(input("Enter number of stars and X:"))
for i in range(1, n+1):
    if i % 2 == 0:
        print("*",end=' ')
    else:
        print("X",end=' ')
print()
