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
    self.startRound(self.playerOne)

  def startRound(self, player):
    player.rollDices(self.dices)
    
    pairs = player.countDicesPair()

    self.view.renderPairs(pairs)
  
  def didPlayerRollSmallStraight(self, player, dices):
    return self.playerOne.lookForSmallStraight(dices)

  def didPlayerRollForBigStraight(self,player, dices):
    return self.playerOne.lookForBigStraight(dices)

  def didPlayerRollRollYatzy(self, player, dices):
    return player.lookForYatzy(dices)
  
  def playerChose(self):
    ##self.playerOne.saveDicesPairs(6)
    ##self.view.renderDices(self.playerOne)
    print("Player chose")