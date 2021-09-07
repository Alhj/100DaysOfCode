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

  def renderDices(self, player):
    for dice in player.dices:
      print(dice.getValue())