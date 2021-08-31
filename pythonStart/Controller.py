import View
import Model

from time import sleep

class Controller:
  def __init__(self):
    self.view = View.View()
    self.model = Model.Model()

  def start(self):
      input = self.view.getUserInput()

      validation = self.model.validateInput(input)

      print(validation)

      self.view.clearConsole()