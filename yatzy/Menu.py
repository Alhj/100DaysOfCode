import os
from keyboard import add_hotkey, wait, unhook_all_hotkeys
from Enum import Enum
  
class Menu:
  selected = 1  
  withMenu = ""

  def start(self):
    for i in range(1,5):
      print("{1} {0} . Do Somthing {0}  {2}".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "))
  

  def renderWithMenu(self):
    os.system('cls' if os.name=='nt' else 'clear')
    self.start()

    
  def up(self):
    self.selected
    if self.selected == 1:
      return
    self.selected -= 1
    self.renderWithMenu()

  def down(self):
    self.selected
    if self.selected == 4:
      return    
    self.selected += 1
    self.renderWithMenu()


  def render(self):
      self.renderWithMenu()
      add_hotkey('up', self.up)
      add_hotkey('down', self.down)
      wait('enter')
      self.end()
  
  def end(self):
    self.selected = 1
    unhook_all_hotkeys()