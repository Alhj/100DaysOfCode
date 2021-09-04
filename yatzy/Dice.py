from random import randint

class Dice:
  value = 0

  def roll(self):
    self.value = randint(1,6)

  def getValue(self):
    return self.value
