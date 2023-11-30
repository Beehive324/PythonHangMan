import random

print("H A N G M A N")
#print("The game will be available soon", end = ".")
words = ["python","java","swift","javascript"]
word = random.choice(words)

user_input = str(input("Guess the word:" + ('-' * len(word)).replace('---', word[:3], 1)))

if user_input == word:
    print("You survived!")
else:
    print("You lost!")
