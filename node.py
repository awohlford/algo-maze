class Node:
  def __init__(self, num, color):
    self.num = num
    self.color = color
    
  def __eq__(self, node):
    if self.num == node.num and self.color == node.color:
      return True
    else:
      return False
