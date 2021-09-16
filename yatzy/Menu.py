import os
from keyboard import add_hotkey, wait, unhook_all_hotkeys
from Enum import renderMenu
  
class Menu:
  selected = 0 
  withMenu = ""
  
  def __init__(self):
    self.enum = renderMenu()
  

  def start(self):
    items = ['start game', 'end application']
    for i in range(0,2):
      print("{1} {0} {2}".format(items[i],">" if self.selected == i else " ", "<" if self.selected == i else " "))
  

  def renderWithMenu(self):
    os.system('cls' if os.name=='nt' else 'clear')
    if self.withMenu == self.enum.renderStart:
      self.start()
      return
    elif self.withMenu == self.enum.smallStraightRender:
      return
    elif self.withMenu == self.enum.bigStraightRender:
      return
    
    
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

  def smallStraightRender(self):
    print("you roll a Small straight")
    return

  def render(self, menu):
      self.renderWithMenu(menu)
      add_hotkey('up', self.up)
      add_hotkey('down', self.down)
      wait('enter')
      self.end()
  
  def end(self):
    self.selected = 1
    unhook_all_hotkeys()