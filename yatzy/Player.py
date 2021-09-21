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
    return pairs

  def saveDicesPairs(self, value):
    dices = []
    for dice in self.dices:
      if dice.getValue() == value:
        self.saveDices.append(dice)
      else:
        dices.append(dice)
    self.dices = dices

  def choseOnes(self):
    return

  def choseTwos(self):
    if self.scoreBord.onePair == '-':
        
      return

    return

  def choseThrees(self):
    if self.scoreBord.threePair == '-':
      return
    return
  
  def choseFours(self):
    if self.scoreBord.fourPair == '-':
      return
  
    return


  def lookForSmallStraight(self, pairs):
    if self.scoreBord.smallStraight == '-':
      sortPairs = sorted(pairs)
      exist = sortPairs == [1,2,3,4,5]
      return exist
      
    return False
    
  def lookForBigStraight(self, pairs):
    if self.scoreBord.bigStraight == '-':
      sortPairs = sorted(pairs)
      exist = sortPairs == [2,3,4,5,6]
      return exist
    
    return False

  def lookForYatzy(self, pairs):
    if self.scoreBord.yatzy == '-':
      sort = sorted(pairs)
      return sort.count(sort[0]) == len(sort)
      
    return False

  def endRound(self):
    self.dices = []
    self.pairs = []
    self.saveDices = []

    