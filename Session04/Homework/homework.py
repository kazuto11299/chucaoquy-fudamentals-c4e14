sent = str(input("Enter a sentence: "))
sen = sent.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count_character = {}
for character in sen:
    if character in alphabet:
        if character in count_character:
            count_character[character] += 1
        else:
            count_character[character] = 1
for i in count_character:
    print(i, count_character[i])
