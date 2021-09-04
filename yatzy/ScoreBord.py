class ScoreBord:
  onePair = 0
  twoPair = 0
  threePair = 0
  fourPair = 0
  smallStraight = 0
  bigStraight = 0
  fullHouse = 0
  chance = 0
  yatzy = 0

  def setOnePair(self, value):
    if(self.onePair == 0):
      self.onePair = value

  def setTwoPair(self, value):
    if(self.twoPair == 0):
      self.twoPair = value
  
  def setTheePair(self, value):
    if(self.threePair == 0):
      self.threePair = value
  
  def setFourPair(self, value):
    if(self.fourPair == 0):
      self.fourPair = value
  
  def setSmallStraight(self):
    if(self.smallStraight == 0):
      self.smallStraight = 15
  
  def setBigStraight(self):
    if(self.bigStraight == 0):
      self.bigStraight = 20

  def setChance(self, value):
    if(self.chance == 0):
      self.chance = value

  def setYatzy(self):
    if(self.yatzy == 0):
      self.yatzy = 50