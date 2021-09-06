from GameBord import GameBord
from Dice import Dice

dices = []

for x in range(6):
  dice = Dice()
  dices.append(dice)


gamebord = GameBord(dices)

gamebord.startGame()