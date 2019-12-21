import string

# The gallows that the hangman will 'use'
hangmanRepr ='''
        ____________
        |---------- \\
        |          ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
                   ||
_________________ /  \\'''


class Hangman():
    def __init__(self, word):
        self.word = word
        self.guessedLetters = list()
    
    def getMistakes(self):
        # Returns the number of incorrect guesses from the player
        wordSet = set(self.word)
        missedSet = set()
        for letter in self.guessedLetters:
            if letter not in wordSet:
                missedSet.add(letter)
        return len(missedSet)
    
    def disp(self):
        # Displays the hangman and guess
        self.dispHangman()
        self.dispLetters()
    
    def dispHangman(self):
        # Displays the hangman
        mistakes = self.getMistakes()
        outLines = hangmanRepr.split("\n")

        # Using carriage return, add parts of hangman on to gallows
        if mistakes >= 6:
            outLines[8] += "\r         \\"
            outLines[9] += "\r          \\_"
        if mistakes >= 5:
            outLines[8] += "\r       /"
            outLines[9] += "\r     _/"
        if mistakes >= 4:
            outLines[6] += "\r          \\"
            outLines[7] += "\r           \\"
        if mistakes >= 2:
            outLines[6] += "\r       | |"
            outLines[7] += "\r       |_|"
        if mistakes >= 3:
            outLines[6] += "\r      /"
            outLines[7] += "\r     /"
        if mistakes >= 1:
            outLines[4] += "\r       _M_"
            outLines[5] += "\r       (_)"
        
        # Print out the hangman
        for line in outLines:
            print(line)
        
    def dispLetters(self):
        # Displays the guessed letters and current word status
        outStr = "\n"
        letterSet = set(self.guessedLetters)

        # Print the word with underscores for un-guessed letters
        for letter in self.word:
            if letter in letterSet:
                outStr += letter + " "
            else:
                outStr += "_ "
        print(outStr)

        # Print out guessed letters
        print("\nGuessed Letters:")
        for letter in self.guessedLetters:
            print(letter, end=" ")
        print()
    
    def getGuess(self):
        # Get and validate user input for a guess
        guess = input("Guess a letter: ")
        while len(guess) != 1 or guess not in string.ascii_letters or guess in self.guessedLetters:
            print("That wasn't a valid letter, please try again...")
            guess = input("Guess a letter: ")
        self.guessedLetters.append(guess.lower())
    
    def hasWon(self):
        # Determines if the player has won
        setGuesses = self.guessedLetters
        for letter in self.word:
            if letter not in setGuesses:
                return False
        return True