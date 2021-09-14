import os
from keyboard import add_hotkey, is_pressed, wait
  
class Menu:
  selected = 1  

  def renderSmall(self):
    self.selected
    os.system('cls' if os.name=='nt' else 'clear')
    for i in range(1,5):
      print("{1} {0} . Do Somthing {0}  {2}".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "))
    
    
  def up(self):
    self.selected
    if self.selected == 1:
      return
    self.selected -= 1
    self.renderSmall()

  def down(self):
    self.selected
    if self.selected == 4:
      return    
    self.selected += 1
    self.renderSmall()


  def render(self):
      self.renderSmall()
      add_hotkey('up', self.up)
      add_hotkey('down', self.down)
      wait('enter')