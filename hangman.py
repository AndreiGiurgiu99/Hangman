
import random

#List of words that are available to be guessed
words=['andrei','iulia','neveon']
lives = 5

#Generates the secret word
def WordGenerator(words):

    #Separate the letters in the string
    global guess_word 
    guess_word  = list(random.choice(words))

    print(f'The word you need to guess has {len(guess_word)} letters')

WordGenerator(words)
print(guess_word)


#Functions that let's the player guess the letters
def GuessTheWord():
    global letters
    letters = []

    for i in guess_word:
        letters.append('?')
    print(letters)

    while letters != guess_word:
        guess = input('Guess a letter: \n')
       
        for i in range(len(guess_word)):
            if guess_word[i] == guess:
                letters[i] = guess
                print(letters)
            
    letters = []
    
    if letters == guess_word:
        print("Good job you've won")

GuessTheWord()