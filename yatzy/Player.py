from collections import Counter
from ScoreBord import ScoreBord


class Player:
  dices = []
  pairs = []
  saveDices = []
  rolls = 0

  def __init__(self):
    self.scoreBord = ScoreBord()

  def rollDices(self, dices):
      if self.rolls < 3 :
        for dice in dices:
          dice.roll()
      
        self.dices = dices
        self.rolls += 1
  
  def countDicesPair(self):
    values = []
    for dice in self.dices:
      values.append(dice.getValue())

    pairs = Counter(values)
    return pairs

  def saveDicesPairs(self, value, dices):
    saveThisdices = []
    for dice in dices:
      if dice.getValue() == value:
        self.saveDices.append(dice)
      else:
        saveThisdices.append(dice)

  def choseOnes(self):
    if self.scoreBord.onePair == '-':
        times = 0
        for dice in self.saveDices:
          if dice.getValue() == 1:
            times += 1
        self.scoreBord.setOnePair(times * 1)
    return

  def choseTwos(self):
    if self.scoreBord.onePair == '-':
        times = 0
        for dice in self.saveDices:
          if dice.getValue() == 2:
            times += 1
        self.scoreBord.setTwoPair(times * 2)
    return

  def choseThrees(self):
    if self.scoreBord.threePair == '-':
      times = 0
      for dice in self.saveDices:
        if dice.getValue() == 3:
          times += 1
      self.scoreBord.setTheePair(times * 3)
    return
  
  def choseFours(self):
    if self.scoreBord.fourPair == '-':
      times = 0
      for dice in self.saveDices:
        if dice.getValue() == 4:
          times += 1
      self.ScoreBord.setFourPair(times * 4)
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

  