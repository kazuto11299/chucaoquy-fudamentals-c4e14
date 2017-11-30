from random import randint
n = randint(1, 100)
guess_wrong = True
while True:
    a = int(input("Guess my number:"))
    if a > n:
        print("Smaller than that")
    elif a == n:
        print("Bingo!")
        break
    else:
        print("Bigger than that")
