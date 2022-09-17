import random
from hangmanpieces import hangman

#List of words that are available to be guessed
words=['andrei','iulia','neveon','cicinelu','gaoaza','biliboaca']
hangman.reverse()

#Generates the secret word
def WordGenerator(words):

    #Separate the letters in the string
    global guess_word 
    guess_word  = list(random.choice(words))

    print(f'The word you need to guess has {len(guess_word)} letters')
    print(hangman[6])

WordGenerator(words)



#Functions that let's the player guess the letters
def GuessTheWord():
    global letters
    letters = []
    lives = 6
    
    for i in guess_word:
        letters.append('?')
    print(letters)

    while letters != guess_word:
        guess = input('Guess a letter: \n')
        
        
        if guess not in guess_word:
            lives -= 1
            
            print(hangman[lives])
            
            if lives == 0:
                print('O no, you lost!')
                break
            else:
                
                print(f"Letter not in word you have only {lives} lives left!")
            
            
        elif guess in letters:
            print("You've tried it already!")

        else: 
            for i in range(len(guess_word)):
                if guess_word[i] == guess:
                    letters[i] = guess
                    print(letters)

    if letters == guess_word:
        print(f"Good job you've won the word is: {''.join(letters)}")
        letters = []
    
                    
GuessTheWord()