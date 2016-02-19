#!/usr/local/bin/python3

import random, sys
from gamestate import GameState

"""
The main class for the game
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


    """
    Generate the keys for the hit map!
    """
    def __hit_location(self):
        if  self.guess < self.gs.villain.target:
            return "low"
        if  self.guess > self.gs.villain.target:
            return "high"
        if  self.guess == self.gs.villain.target:
            return "on"


    """
    The player has guessed, let's resolve where. Here we are using a sort of switch system that Python uses. In truth,
    we are relying on the fact that functions can be bound to variables. In this case, to keys in a dictionary.
    """
    def __resolve_guess(self):
        loc = self.__hit_location()
        self.hits[loc]()

        if (self.gs.player.life <= 0):
            self.lose()


    """
    After a player guesses and does not hit the target, he gets hit. The closer he is, the harder he's hit.
    """
    def __resolve_hit(self):
        hit = 20 - abs(self.guess - self.gs.villain.target) + random.randint(0,5)
        if hit < 0:
            hit = 0

        self.gs.player.life -= hit
        return hit

    """
    resolve a hit below the target number
    """
    def __hit_low(self):
        print("You attack was too low!")
        hit = self.__resolve_hit()
        print("You got hit for " + str(hit) + " damage! You have " + str(self.gs.player.life) + " life left.")


    """
    resolve a hit above the target number
    """
    def __hit_high(self):
        print("You attack was too high!")
        hit = self.__resolve_hit()
        print("You got hit for " + str(hit) + " damage! You have " + str(self.gs.player.life) + " life left.")


    """
    resolve a guess that is square on the target
    """
    def __hit_on(self):
        self.win()


    """
    Do the work to win the game.
    """
    def win(self):
        print("You got it! You win! You killed " + self.gs.villain.name + ".")
        self.game_on = False

    """
    Do the work to lose the game
    """
    def lose(self):
        print("OUCH, you are dead. You Lose. Game over. Go home. Get better at guessing.")
        self.game_on = False


    """
    The main function to start the game.
    """
    def run(self):
        # the initial game message
        print("Welcome to the rogue-like game of your life, GUESS THE NUMBER, VS! ")
        print("You have been assinged the name " + self.gs.player.name)
        print("You will be fighting " + self.gs.villain.name)
        print("Guess a number between 1 and 100. The closer you are, the harder your opponent hits. Hit him once and you win. Run out of life and you die.")

        # Run the game while it suppose to be running
        while self.game_on:
            self.__ask_for_guess()
            self.__resolve_guess()

        print("Thanks for playing. Please send your money to walt.norblad@gmail.com")


"""
MAIN BODY
"""

g = Game()
g.run()