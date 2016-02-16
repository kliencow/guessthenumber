#!/usr/local/bin/python3

import random

"""
  A very simple Game class for the simlest form of the game. It may have been even simpler without a class,
  but we need to keep some standards high.
"""
class Game:

    def __init__(self):
        self.number = random.randint(1,100)
        self.guess = -1

    """
        The main function to start the game. It's also all of the game logic.
    """
    def run(self):
        # This is a game loop. They often look like this, a loop with no exit condition. These styles of loops rely on
        # native loop controls to stop the game. Note: continue jumps the code back to the start of the loop again
        # and checks conditions. break exits the loop without checking conditions.
        while True:
            if self.guess < 0:
                print("Welcome to the game of your life, GUESS THE NUMBER! You have not guessed yet.")
                print("Guess a number between 1 and 100")
            elif self.guess < self.number:
                print("Your guess is low.")
            elif self.guess > self.number:
                print("Your guess is too high.")
            elif self.guess == self.number:
                print("You got it! You win!")
                break
            else:
                # does this need to be here? What is a good way to exlude it?
                print("YOU SHOULD NOT BE HERE... GO AWAY.")

            # this totally works, but it's not ideal. What sort of problems might arise from this code?
            self.guess = int(input("Your guess? "))

"""
MAIN BODY
"""

g = Game()
g.run()