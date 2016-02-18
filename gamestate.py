import util
import random

class GameState:

    def __init__(self):
        self.player = Player()
        self.villain = Villain()
        self.score = 0
        # set the last high score
        self.high_score = self.__load_high_score()
        # flag to determine if we should set the first time message for the game
        self.firstTime = True


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


class Mob:
    def __init__(self):
        self.name = util.create_random_name()


class Player(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.life = 50


class Villain(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.target = random.randint(1, 100)
