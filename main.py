#!/usr/local/bin/python3

import random, sys
from gamestate import GameState

"""
  A simple game, but with a win condition and high score tracking!

  We also started to use helper functions, basic IO, simple signal processing, recursion, and even try clauses.
"""
class Game:
    def __init__(self):
        self.gs = GameState()
        self.game_on = True
        self.hits = {
            "high": self.__hit_high,
            "low" : self.__hit_low,
            "on"  : self.__hit_on,
        }


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

    def __hit_location(self):
        if  self.guess < self.gs.villain.target:
            return "low"
        if  self.guess > self.gs.villain.target:
            return "high"
        if  self.guess == self.gs.villain.target:
            return "on"

    def __resolve_guess(self):
        loc = self.__hit_location()
        self.hits[loc]()

        if (self.gs.player.life <= 0):
            self.lose()



    def __resolve_hit(self):
        hit = 20 - abs(self.guess - self.gs.villain.target) + random.randint(0,5)
        if hit < 0:
            hit = 0

        self.gs.player.life -= hit
        return hit

    def __hit_low(self):
        print("You attack was too low!")
        hit = self.__resolve_hit()
        print("You got hit for " + str(hit) + " damage! You have " + str(self.gs.player.life) + " life left.")

    def __hit_high(self):
        print("You attack was too high!")
        hit = self.__resolve_hit()
        print("You got hit for " + str(hit) + " damage! You have " + str(self.gs.player.life) + " life left.")

    def __hit_on(self):
        self.win()


    """
    Do the work to win the game.
    """
    def win(self):
        print("You got it! You win! You killed " + self.gs.villain.name + ".")
        self.game_on = False

    def lose(self):
        print("OUCH, you are dead. You Lose. Game over. Go home. Get better at guessing.")
        self.game_on = False


    """
    The main function to start the game.
    """
    def run(self):
        print("Welcome to the rogue-like game of your life, GUESS THE NUMBER, VS! ")
        print("You have been assinged the name " + self.gs.player.name)
        print("You will be fighting " + self.gs.villain.name)
        print("Guess a number between 1 and 100. The closer you are, the harder your opponent hits. Hit him once and you win. Run out of life and you die.")

        while self.game_on:
            self.__ask_for_guess()
            self.__resolve_guess()





"""
MAIN BODY
"""

g = Game()
g.run()