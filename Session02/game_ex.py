from random import randint
x = randint(0, 2)
print("Agi:", x)
y = randint(0, 2)
print("Luck:", y)
n = randint(1, 6)

if n > x + y:
    print("You took damage")
else:
    print("Dodged the attack")
