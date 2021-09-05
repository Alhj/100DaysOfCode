from collections import Counter
from ScoreBord import ScoreBord

class Player:
  dices = []
  pairs = []

  def __init__(self):
    self.scoreBord = ScoreBord()

  def rollDices(self, dices):
      for dice in dices:
        dice.roll()
      
      self.dices = dices
  
  def countDicesPair(self):
    pairs = Counter(self.dices)
    print(pairs)

  def endRound(self):
    self.dices = []
    self.pairs = []