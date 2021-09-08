from collections import Counter
from ScoreBord import ScoreBord

class Player:
  dices = []
  pairs = []
  saveDices = []

  def __init__(self):
    self.scoreBord = ScoreBord()

  def rollDices(self, dices):
      for dice in dices:
        dice.roll()
      
      self.dices = dices
  
  def countDicesPair(self):
    values = []
    for dice in self.dices:
      values.append(dice.getValue())

    pairs = Counter(values)
    print(pairs.most_common())
    return pairs

  def saveDicesPairs(self, value):
    dices = []
    for dice in self.dices:
      if dice.getValue() == value:
        self.saveDices.append(dice)
      else:
        dices.append(dice)
    self.dices = dices

  def endRound(self):
    self.dices = []
    self.pairs = []
    self.saveDices = []

    