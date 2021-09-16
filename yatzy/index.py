from GameBord import GameBord
from Dice import Dice
from Menu import Menu
from Enum import InputEnum

dices = []

for x in range(5):
  dice = Dice()
  dices.append(dice)


menu = Menu()

menu.renderWithMenu()