numbers  = [1, 6, 8, 1, 2, 1, 5, 6]
n = False

while not n:
    try:
        a = int(input("Enter a number: "))
        n = True
    except ValueError:
        print("Not a number!")
occurences = numbers.count(a)
print("{0} appears {1} times in my list".format(a, occurences))
