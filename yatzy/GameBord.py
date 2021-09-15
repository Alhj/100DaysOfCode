from Player import Player
from View import View
from Menu import Menu
from Enum import Enum
import keyboard

class GameBord:
  def __init__(self, dices):
    self.dices = dices
    self.playerOne = Player()
    self.view = View();
    self.menu = Menu();

  def startGame(self):
    self.startRound()

  def startRound(self):
    self.playerOne.rollDices(self.dices)
    pairs = self.playerOne.countDicesPair()
    
    if self.playerOne.lookForSmallStraight(pairs):
      print("hello")
    elif self.playerOne.lookForBigStraight(pairs):
      self.menu
    else:
      self.playerChose()


  def playerChose(self):
    ##self.playerOne.saveDicesPairs(6)
    ##self.view.renderDices(self.playerOne)
    print("Player chose")