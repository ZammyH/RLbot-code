# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        speed=400
        self.set_intent(drive(500))
        Print(f'my x postion is:{self.me.location.x}')
        # create a "cooler and warmer featre"
        # on top of that make a direction thing in the gaing window where i am ponited here th opposing goal is!
        # think of a game feature that is so good that its a cheat; ask firdowsa what she would like to cheat in game; and ask what you need. more like what you need to not suck at
        #Insert Machine Learning in here i need ti win




        