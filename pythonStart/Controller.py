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

      self.view.clearConsole()

      if validation == False:
          self.noInput()
      else:
        self.askUserToSaveData(input)

  def noInput(self):
    self.view.noInput()
    self.start();

  def askUserToSaveData(self, input):
    self.view.saveInput()
    self.model.writeText( '\n' + input)
    
