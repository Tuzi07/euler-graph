class Node:
  def __init__(self):
    self.edges = {}
    self.was_visited = False
  
  def print_edges(self):
    for edge in self.edges:
      print(edge, end = ' ')
    print()
  
  def degree(self):
    return len(self.edges)
  
  def is_adjacent(self, node):
    for edge in self.edges:
      if node == edge:
        return True
    return False
