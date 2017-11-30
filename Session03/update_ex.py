menu = ['Yi', 'Riven', 'Daxua']
# for i in range(len(menu)):
#     print(i+1,".", menu[i])
# m = input("Position you want to update? ")
# n = input("Your replacing favorite? ")
# menu.append
for i, item in enumerate(menu):
    print(i+1, item, sep=". ")

position = int(input("Enter position to update: "))
new_item = input("Replacing menu? ")
menu[position - 1] = new_item
for i, item in enumerate(menu):
    print(i+1, item, sep=". ")
