from keyboard import add_hotkey, wait

class Menu:
  
  selected = 1  
  
  def renderSmall(self):
    print("\n" * 30)
    for i in range(1,5):
      print("{1} {0} . Do Somthing {0}  {2}".format(i, ">" if self.selected == i else " ", "<" if self.selected == i else " "))
    self.key()
    wait()
    
  def up(self, renderMenu):
    if self.selected == 1:
      return
    
    self.selected -= 1
    self.renderSmall()

  def down(self, renderMenu):
    if self.selected == 4:
      return
    
    self.selected += 1
    self.renderSmall()

  
  def key(self):
    add_hotkey("up", self.up)
    add_hotkey("down", self.down)