class Model:
  path = 'userInput.txt'

  def validateInput(self, input):
    if len(input) != 0 :
      return True
    else: 
      return False

  def getText(self): 
    f = open(self.path, "r")
    values = f.readlines()
        
    f.close();
    return values

  def writeText(self, input):
    f = open(self.path,"a")

    f.writelines(input)

    f.close()