import random

word = ""

with open("WordsForGames.txt") as word_file:
    words = word_file.read().split() #This splits by whitespace, if you used some other delimiter specify the delimiter here as an argument.
    while len(word) < 2:
        word = random.choice(words)

displayed_word = []
used_letters = []
lives = 6

print("Welcome to the Hangman game! You have 6 guesses")


for x in word:
    displayed_word.append(" _ ")


while lives > 0:
    
    print(', '.join(displayed_word))
    print("used letters:")
    print(', '.join(used_letters) + "\n")
    letter = input("Pick a letter:")


    if letter in word: 
        index = 0
        while index < len(word):
            index = word.find(letter, index)
            if index == -1:
                break
            
            displayed_word[index] = letter
            index = index + 1
        
        print("\nYou chose the correct letter!\n")

    else:
        used_letters.append(letter)
        lives = lives - 1
        print("\nLetter ", letter.upper(), " is not in the word.")
        print("You have ", lives, " lives remaining\n")

    if word == ''.join(displayed_word):
        print(displayed_word)
        print("You WIN the game!")
        quit()

print ("Game over!")
print('The correct word is: ', word)