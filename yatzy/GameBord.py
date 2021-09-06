from Player import Player
import keyboard

class GameBord:
  def __init__(self, dices):
    self.dices = dices
    self.playerOne = Player()

  def startGame(self):
    self.startRound()

  def startRound(self):
    self.playerOne.rollDices(self.dices)
    self.playerOne.countDicesPair()
    
    while True:
      if keyboard.is_pressed('s'):
        print('saveprint')
      elif keyboard.is_pressed('n'):
        print('no save')