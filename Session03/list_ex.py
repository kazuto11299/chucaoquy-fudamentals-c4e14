print("Hi there, here are your favorite things so far")
menu = ['Yi', 'Riven', 'Daxua']
print(*menu, sep=', ')
n = input("Name one thing you want to add: ")
menu.append(n)
print(*menu, sep=', ')
