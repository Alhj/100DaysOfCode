from pathlib import Path

class Model:
  pathToFile = 'userInput.txt'
  def __init__(self):
    
    self.path = Path(self.pathToFile)

  def validateInput(self, input):
    if len(input) != 0 :
      return True
    else: 
      return False

  def getText(self):
    values = ['no file found']
    if self.path.is_file():
      f = open(self.pathToFile, "r")
      values = f.readlines()
        
      f.close();
    
    return values

  def writeText(self, input):
    if self.path.is_file():
      f = open(self.pathToFile,"a")
      f.writelines(input)
      f.close()
    else:
      f = open(self.pathToFile, "w")
      f.writelines(input)
      f.close()
