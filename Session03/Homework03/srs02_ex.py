# 2.1
sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello! My name is Quý and these are my sheeps' sizes")
print(*sheep, sep = ", ")
print()
# 2.2
king_sheep = max(sheep)
print("My biggest sheep's size: ", king_sheep, "Let's shear it!")
# 2.3
poor_sheep = sheep.index(max(sheep))
default = 8
sheep[poor_sheep] = default
print("After shearing, my sheeps' sizes are: ")
print(*sheep, sep = ", ")
print()
# 2.4 + 2.5
n = 1
for a in range(n):
    for i in range(len(sheep)):
        growth = sheep[i] + 50
        sheep[i] = growth
    print("After a month, here are my sheeps' sizes:")
    print(*sheep, sep = ", ")
m = int(input("How many months? "))
for x in range(m):
    print("Months: ", x + 2)
    for j in range(len(sheep)):
        grow = sheep[j] + 50
        sheep[j] = grow
    print("After a while, here are my sheeps' sizes:")
    print(*sheep, sep = ", ")
# 2.6
print("My flock's size in total: ", sum(sheep))
print("I would get: ", sum(sheep) * 2, "$")
