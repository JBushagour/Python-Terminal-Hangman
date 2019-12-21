import os
import random
from HangmanClass import Hangman


def main():
    # Startup message
    clearTerminal()
    print("-=" * 15 + " Welcome to Hangman " + "=-" * 15)

    # Flag for setting up the hangman
    initialRun = 1

    while True:
        # Set up hangman
        if initialRun:
            # Hangman created with random word
            hangman = Hangman(getWord())
            hangman.disp()
            initialRun = 0
        
        hangman.getGuess()
        clearTerminal()
        hangman.disp()
        
        # Determines if player has won/lost yet
        if gameEnd(hangman):
            # Ask if player wants to play again/end
            choice = getNewGame()
            clearTerminal()
            if choice == "y":
                # Start new game
                intitalRun = 1
            else:
                # End
                break


def clearTerminal():
    # if operating system is unix-based, the "cls" command is run
    # otherwise, "clear" if run (this handles windows terminal)
    os.system('cls' if os.name == 'nt' else 'clear')


def getWord():
    # reads file of words and returns a random one
    with open("words.txt", "r") as words:
        lines = words.readlines()
    return random.choice(lines).lower()[:-1]


def getNewGame():
    # Validates user input to see if they want to play again
    choice = input("Play again? y/n: ")
    while choice.lower() not in ["y", "n", "yes", "no"]:
        choice = input("Play again? y/n: ")
    
    # Return a "y" or "n" even if they said "yes"/"no"
    return choice[0]


def gameEnd(hangman):
    # Returns if the game should end
    end = 0

    # Made too many mistakes
    if hangman.getMistakes() == 6:
        end = 1
        print("You've lost :(")
        print("The word was " + hangman.word)
    
    # The player has guessed the word
    elif hangman.hasWon():
            end = 1
            print("You've won! :)")
    return end


if __name__ == '__main__':
    main()
