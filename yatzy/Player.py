class Player:
  dices = []
  pairs = []

  def rollDices(self, dices):
      for dice in dices:
        dice.roll()
      
      self.dices = dices
  
  def countDicesPair(self):
    self.dices

  def endRound(self):
    self.dices = []
    self.pairs = []