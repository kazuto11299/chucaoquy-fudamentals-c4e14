from random import *
import random
print("Welcome to Word Jumble!")
print("Can you guess the word?")
word_library = ["yasuo", "overrated", "destroyer", "assasin", "blademaster", "nigga", "wellplayed"]
pick_random = choice(word_library)
character = list(pick_random)
random.shuffle(character)
print(*character)
guess = input("Your answer is? ")
if guess == pick_random:
    print("Congratulations! Your answer is correct!")
else:
    print("Incorrect answer! Try again!")
