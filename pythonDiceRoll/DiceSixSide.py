import random
  
class DiceSixSide:
    def __init__(self): 
      self.value = 0

    
    def roll(self):
      self.value = random.randint(1,6)
    

    def showValue(self):
      return self.value
