import csv
from node import Node
from edge import Edge

class Graph:
  def __init__(self, nodes_filepath, edges_filepath):
    self.nodes = {}
    self.number_of_nodes = 0
    self.number_of_edges = 0
    self.add_nodes_from_csv(nodes_filepath)
    self.add_edges_from_csv(edges_filepath)

  def add_node(self, node):
    if node in self.nodes:
      print("This node already exists")
    else: 
      self.nodes[node] = Node()
      self.number_of_nodes += 1

  def add_edge(self, origin, destiny, weight):
    if origin not in self.nodes or destiny not in self.nodes:
      print("Node does not exist")
    else:
      self.nodes[origin].edges[destiny] = Edge(weight = int(weight))
      self.nodes[destiny].edges[origin] = Edge(weight = int(weight))
      self.number_of_edges += 1

  def add_nodes_from_csv(self, nodes_filepath):
    with open(nodes_filepath, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.add_node(row[0])

  def add_edges_from_csv(self, edges_filepath):
    with open(edges_filepath, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.add_edge(origin = row[0], destiny = row[1], weight = row[2])

  def print_graph(self):
    for node in self.nodes:
      print(node, "-> ", end = '')
      self.nodes[node].print_edges()

  def has_edge(self, node1, node2):
    if node1 not in self.nodes or node2 not in self.nodes:
      return False
    if node1 == node2:
      return True
    return self.nodes[node1].is_adjacent(node2)

  def is_complete(self):
    from math import comb
    return self.number_of_edges == comb(self.number_of_nodes, 2)

  def remove_edge(self, node1, node2):
    if node1 not in self.nodes or node2 not in self.nodes:
      print("Node does not exist")
    else:
      self.nodes[node1].edges.pop(node2)
      self.nodes[node2].edges.pop(node1)
      self.number_of_edges -= 1

  def reset_visited_nodes(self):
    for node in self.nodes:
      self.nodes[node].was_visited = False
  
  def dfs_count_from_node(self, node):
    visited_nodes = 1
    self.nodes[node].was_visited = True
    for destiny in self.nodes[node].edges:
      if not self.nodes[destiny].was_visited:
        visited_nodes += self.dfs_count_from_node(destiny)
    return visited_nodes
