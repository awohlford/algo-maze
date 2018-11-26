class Edge:
  def __init__(self, start, end, color):
    self.start = start
    self.end = end
    self.color = color

  def __eq__(self, other):
    if self.start == other.start and self.end == other.end and self.color == other.color:
      return True
    else:
      return False
