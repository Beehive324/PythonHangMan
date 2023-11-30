import random

attempts = 8
print("H A N G M A N " ,"#" ,attempts, "attempts")
#print("The game will be available soon", end = ".")
words = ["python","java","swift","javascript"]
word = random.choice(words)

word_list = list(word)
guessed_word = ''

for _ in range(1,1000): #amount of tries
    user_input = str(input("Input a letter:" + ('-' * len(word))))
    if user_input in word_list:
        attempts -= 1
        guessed_word += user_input
        print(guessed_word,"#" ,attempts, "attempts")
        if attempts == 0:
             print("Thanks for playing!")
             exit()
    elif user_input not in word_list:
        attempts -= 1
        print("That letter doesn't appear in the word.","#" ,attempts, "attempts")
        if attempts == 0:
            print("Thanks for playing!")
            exit()


