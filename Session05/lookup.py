teen_dict = {
    'eny': 'Em người yêu',
    'any': 'Anh người yêu',
    'gấu': 'Người yêu',
    'hk': 'Không'
}
while True:
    for key, value in teen_dict.items():
        print(key, end = " ")
    print()
    print("* " * 10)
    code = str(input("Enter a word to search: ")).lower()
    if code in teen_dict:
        print(code)
        print(teen_dict[code])
    else:
        choice = input("Not found! Do you want to contribute this word (Y/N)? ").lower()
        if choice == 'y':
            translation = input("Translation: ")
            teen_dict[code] = translation
    print('* ' * 10)
