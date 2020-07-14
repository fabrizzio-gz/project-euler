##
# Problem 84
##
# Simulating a monopoly game
# Idea: create a monopoly game simulator
from itertools import cycle
import random

class Monopoly_board():
    
    def __init__(self):
        self.squares = 40
        self.pos = 0
        self.stays = {}
        self.turns = 0
        self.double = 0
        self.cc = cycle(range(16)) # 16 comunity chest cards
        self.cc_squares = [2, 17, 33]
        self.ch = cycle(range(16)) # 16 chance cards
        self.ch_squares = [7, 22, 36]
        self.ch_cards = {0:0, 1:10, 2: 11, 3: 24, 4: 39, 5: 5}

    def play(self, dice):
        self.turns += 1
        throw_1 = dice.throw()
        throw_2 = dice.throw()
        triple_double = False
        # Check double
        if throw_1 == throw_2:
            self.double += 1
            # Check triple double
            if self.double == 3:
                self.pos = 10
                triple_double = True
                self.double = 0
        else:
            self.double = 0
        if not triple_double:
            self.pos = (self.pos + throw_1 + throw_2) % self.squares
            # Check if go to jail (square 30)
            if self.pos == 30:
                self.pos = 10
                # Check comunity chest:
            if self.pos in self.cc_squares:
                cc = self.get_cc()
                if cc == 0:
                    # Go to Go
                   self.pos = 0
                elif cc == 1:
                    self.pos = 10
                    # Check chance squares:
            elif self.pos in self.ch_squares:
                ch = self.get_ch()
                # Cards that move to a certain position
                if ch < 6:
                    self.pos = self.ch_cards[ch]
                    # cards that move to a relative position
                elif ch < 10:
                    if ch == 6 or ch == 7:
                        self.pos = self.next_railway()
                    elif ch == 8:
                        self.pos = self.next_utility()
                    else:
                        self.pos -= 3
        
        # Update stays
        self.stays[self.pos] = self.stays.get(self.pos, 0) + 1

    def next_utility(self):
        if self.pos <= 12:
            return 12
        elif self.pos <= 18:
            return 18
        else:
            return 12

    def next_railway(self):
        if self.pos <= 5:
            return 5
        elif self.pos <= 15:
            return 15
        elif self.pos <= 25:
            return 25
        elif self.pos <= 35:
            return 35
        else:
            return 5      
    
    def get_cc(self):
        return next(self.cc)

    def get_ch(self):
        return next(self.ch)
        
    def get_stays(self):
        return self.stays

    def print_odds(self):
        stays = self.stays.copy()
        # Order dict
        self.stays = {k:v for k,v in sorted(stays.items(), key= lambda item: item[1], reverse = True)}
        for square in self.get_stays():
            odd = round(self.get_stays()[square]/self.turns * 100, 2)
            print(square, ':', odd)

class Dice():
    def __init__(self, size):
       self.number = []
       for i in range(1, size + 1):
           self.number.append(i)

    def throw(self):
        return random.choice(self.number)

def play_turns(monopoly_board, dice, turns):
    for turn in range(turns):
        monopoly_board.play(dice)
    
monopoly_board = Monopoly_board()
n = 4
dice = Dice(n)
turns = 100000
play_turns(monopoly_board, dice, turns)
monopoly_board.print_odds()
