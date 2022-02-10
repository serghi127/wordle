import random
from time import sleep
listofwords = open("textfilesforgames\wordlewords.txt",'r')
listofwords1 = []
# wordindex = random.randint(0, 5756)
# for line in listofwords:
#     listofwords1.append(line.strip()) 
# word = listofwords1[wordindex]
# wordlist = list(word)
numofguesses = 6
gameover = False
playerguess = False
playeringame = True

almostletters = []
correctletters = []
incorrectletters = []

def load():
    print('.')
    sleep(0.2)
    print('..')
    sleep(0.2)
    print('...')
    sleep(0.2)
    print('..')
    sleep(0.2)
    print('.')
    sleep(0.2)

def intro():
    print('Welcome to wordle unlimited! Start the game by entering a 5 letter word.\n'
    'You will have 6 guesses. Try to guess the word before then! Good luck!')
    #print(word)
    sleep(1)

def guessword():
    global gameover
    global numofguesses
    while numofguesses > 0 and gameover == False:
        guess = input("\nEnter a guess. You have " + str(numofguesses) + " left!: ")
        almostletters.clear()
        correctletters.clear()
        if guess.lower() in listofwords1:
            guesslist = list(guess.lower())
            numofguesses -= 1
            if guess.lower() == word.lower():
                print("\nYou guessed the word! The word was " + word.upper() + "! This took you \n"
                + str(6 - numofguesses) + " guess(es)!")
                gameover = True
                break
            
            for letter in guesslist:
                if letter in guesslist and letter in wordlist:
                    if guesslist.index(letter) == wordlist.index(letter):
                            correctletters.append(letter)
                    elif guesslist.index(letter) != wordlist.index(letter):
                        if letter not in almostletters and letter not in correctletters:
                            almostletters.append(letter)
                        
                else:
                    if letter not in incorrectletters:
                        incorrectletters.append(letter)
                        incorrectletters1 = sorted(incorrectletters)

            load()
            print('\nLetters in the right spot: ' + str(correctletters))
            sleep(0.5)
            print('Letters in the wrong spot, but are in the word: ' + str(almostletters))
            sleep(0.5)
            print('Incorrect letters: ' + str(incorrectletters1))
            load()

        else:
            print('Not a real 5-letter word! Guess again!')
            continue

while playeringame:

    if gameover == False:
        wordindex = random.randint(0, 5756)
        for line in listofwords:
            listofwords1.append(line.strip()) 
        word = listofwords1[wordindex]
        wordlist = list(word)
        load()
        intro()
        while numofguesses > 0:
            guessword()

    if gameover == True and numofguesses > 0:
        print('\nGood job! You guessed the word!')
        sleep(1)
        answer = input('Would you like to play again? Press Y for yes and X for no: ')
        if answer.lower() == 'y':
            numofguesses = 6
            incorrectletters.clear()
            load()
            gameover = False
        elif answer.lower() == 'x':
            print("\nThanks for playing!")
            load()
            print('NEW GAME')
            sleep(1)
            exit()

    elif numofguesses == 0:
        gameover = True
        print('\nGame Over! The word was ' + word.upper() + '!')
        sleep(1)
        answer = input("Would you like to play again? Press 'Y' for yes and 'X' for no: ")
        if answer.lower() == 'y':
            numofguesses = 6
            incorrectletters.clear()
            load()
            print('NEW GAME')
            gameover = False
        elif answer.lower() == 'x':
            print("\nThanks for playing!")
            load()
            sleep(1)
            exit()
        else:
            print('Not a valid answer! Try again.')
            continue