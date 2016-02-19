import util
import random

"""
This is a class that helps track the state of the game. These modules/files/classes can get quite complex.
"""
class GameState:

    def __init__(self):
        # the player
        self.player = Player()
        # the player's opponent
        self.villain = Villain()

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
A generic version of a thing that can take action. Right now, there are only two of these
"""
class Mob:
    def __init__(self):
        self.name = util.create_random_name()

"""
The player, who has a name and some life
"""
class Player(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.life = 50

"""
The opponents for the player who has a name and a target number to try to hit
"""
class Villain(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.target = random.randint(1, 100)
