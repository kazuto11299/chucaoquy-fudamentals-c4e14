print("Welcome to our shop!")
shop = ["T-shirt", "Sweater"]
print("Our clothes: ", end = "")
print(*shop, sep =", ")
loop = True
while loop:
    opt = input("Which option do you want (C, R, U D)? ")
    if opt == "C" or opt == "c":
        shop.append(input("Enter new item: "))
        print("New list: ", end = "")
        print(*shop, sep = ", ")
    elif opt == "R" or opt == "r":
        print("Our list: ", end = "")
        print(*shop, sep = ", ")
    elif opt == "U" or opt == "u":
        position = int(input("Update position: "))
        upd = str(input("New item: "))
        shop[position] = upd
        print("New list: ", end = "")
        print(*shop, sep = ", ")
    elif opt == "D" or opt == "d":
        position_ = int(input("Delete position: "))
        del shop[position_ - 1]
        print("New list: ", end = "")
        print(*shop, sep = ", ")
    elif opt == "Q" or opt == "q":
        loop = False
    else:
        print("This option cannot be performed!")
        loop = False


# menu = ['T-Shirt', 'Sweater']
# q = True
# for i, item in enumerate(menu):
#     print(i + 1, item, sep='. ')
# while q:
#     selection = input("Welcome to our shop, what do you want (C, R, U, D)? (Q to quit): ")
#     if (selection == "C"):
#         new_item = input("Enter Your New Item: ")
#         menu.append(new_item)
#         for i, item in enumerate(menu):
#             print(item, sep='. ', end=' ')
#         print(menu, sep =", ")
#     if (upper.selection == "R"):
#         for i,item in enumerate(menu):
#             print(item, sep='. ', end=' ')
#         print()
#
#     if (upper.selection == "U"):
#         position = int(input("Update Position?: "))
#         new = input("New item?: ")
#         if (position > 0 and position < (len(menu) + 1)):
#             menu[position - 1] = new
#             for i,item in enumerate(menu):
#                 print(item, sep='. ', end=' ')
#             print()
#         else:
#             print("It's out of range!")
#
#     if (selection == "D"):
#         position = int(input("Delete Position?: "))
#         if (position > 0 and position < (len(menu) + 1)):
#             menu.pop(position - 1)
#             for i,item in enumerate(menu):
#                 print(item, sep='. ', end=' ')
#             print()
#         else:
#             print("It's out of range!")
#
#     if (selection == "Q"):
#         print("Quit Complete!")
#         q = False
