import random

attempts = 8
print("H A N G M A N " ,"#" ,attempts, "attempts")
#print("The game will be available soon", end = ".")
words = ["python","java","swift","javascript"]
word = random.choice(words)
guess_input = ('_') * len(word)
display = []
for i in word:
    display += "_"
word_list = list(word)
guessed_word = ''
for _ in range(1, 1000):
    user_input = str(input("Input a letter:" + guess_input))
    for position in range(len(word)):
        if user_input == word[position] and user_input not in guessed_word:
            attempts -= 1
            guessed_word += user_input
            display[position]=word[position]
            if attempts == 0:
                print("Thanks for playing!")
                exit()
            elif user_input in guessed_word:
                print()
    print(*display,"#" ,attempts, "attempts")
   
    if user_input not in word_list:
        attempts -= 1
        print("That letter doesn't appear in the word.","#" ,attempts, "attempts")
        if attempts == 0:
            print("Thanks for playing!")
            exit()


