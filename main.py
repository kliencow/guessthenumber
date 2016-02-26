#!/usr/local/bin/python3

import random, sys

"""
  A simple game, but with a win condition and high score tracking!

  We also started to use helper functions, basic IO, simple signal processing, recursion, and even try clauses.
"""
class Game:

    def __init__(self):
        # the number to try to guess
        self.number = random.randint(1,100)
        # the current guess, -1 by default to indicate no guesses
        self.guess = -1
        # set the last high score
        self.high_score = self.__load_high_score()
        # the current number of tries, which the score in this case
        self.tries = 0
        # flag to determine if we should set the first time message for the game
        self.firstTime = True


    """
    Recursively ask for guesses until a valid one is guessed. This has the nice side effect of tallying all of the
    responses after a valid guess is reached. Because this accidentally traps ctrl-c, we have to check for it and
    bubble it up (read - kill the program)
    """
    def __ask_for_guess(self):
        try:
            self.guess  = int(input("Your guess? "))
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("That is not a valid number (integer), let alone one between 1 and 100.")
            self.__ask_for_guess()

        self.tries += 1


    """
    Simple load function to set up previous highscores
    """
    def __load_high_score(self):
        try:
            f = open('high_score.txt', 'r')
            highscore = int(f.read())
            f.close()
            return highscore
        except:
            return 0


    """
    Simple storage function to save high scores
    """
    def __store_high_score(self):
        try:
            f = open('high_score.txt', 'w')
            f.write(str(self.tries))
            f.close()
        except:
            print("Unable to store highscore... this is odd")


    """
    Do the work to win the game. This includes printing messages and saving highscores
    """
    def __win(self):
        print("You got it! You win! You got it in " + str(self.tries) + " tries.")
        if  self.tries < self.high_score or self.high_score == 0:
            print("Congratulations on a new high score! It used to be " + str(self.high_score))
            self.__store_high_score()


    """
    The main function to start the game.
    """
    def run(self):
        # This is a game loop.
        while True:
            if self.firstTime:
                print("Welcome to the game of your life, GUESS THE NUMBER! You have not guessed yet.")
                print("Guess a number between 1 and 100")
                self.firstTime = False
            elif self.guess < self.number:
                print("Your guess is low.")
            elif self.guess > self.number:
                print("Your guess is too high.")
            else: # guess == number
                self.__win()
                break

            self.__ask_for_guess()


"""
MAIN BODY
"""

g = Game()
g.run()