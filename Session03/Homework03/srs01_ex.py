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
