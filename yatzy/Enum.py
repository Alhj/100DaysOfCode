from enum import Enum

class InputEnum(Enum):
  saveDices = "save"
  reRollDices = "reRoll"
  choseOnes = "choseOnes"
  choseTwos = "choseTwos"
  choseThrres = "choseThrres"
  choseFours = "choseFours"
  choseSmallStraight = "choseSmallStraight"
  choseBigStraight = "choseBigStraight"
  choseFullHouse = "choseFullHouse"
  choseChance = "choseChance"
  choseYatzy = "choseYatzy"


class renderMenu(Enum):
  renderStart = "renderStart"
  SaveDices = "saveDices"
  reRollDices = "reRoll"
  smallStraightRender = "RenderSmallStraight"
  bigStraightRender = "RenderBigStraight"
  