from os import system, name

class View:

  def getUserInput(self):
    userInput = input("Enter Number here: ")
    return userInput

  def clearConsole(self):
    if name == 'nt':
      _ = system('cls')

    else:
      _ = system('clear')