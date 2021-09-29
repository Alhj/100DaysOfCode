from keyboard import is_pressed
class View:

  def choseSaveDices(self):
    print('Do you whant to save dices')
    if is_pressed('s'):
      return True
    elif is_pressed('n'):
      return False
    else:
      self.choseSaveDices()

  def renderDices(self, dices):
    for dice in dices:
      print(dice.getValue(), end=" ")

  def renderPairs(self, dicesPair):
    for key, value in dicesPair.items():
      print(key, value)
