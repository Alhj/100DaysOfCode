from os import system, name

class View:

  def getUserInput(self):
    userInput = input("Enter Number here: ")
    return userInput

  def clearConsole(self):
    if name == "nt":
      _ = system("cls")

    else:
      _ = system("clear")

  def noInput(self):
    print("there are no input from user")
  
  def saveInput(self):
    print("Save your input")

