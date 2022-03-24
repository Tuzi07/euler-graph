import csv
from math import comb

class Graph:
  def __init__(self):
    self.adjacency_list = {}
    self.number_of_nodes = 0
    self.number_of_edges = 0

  def from_filepaths(self, nodes_filepath, edges_filepath):
    self.add_nodes(nodes_filepath)
    self.add_edges(edges_filepath)
    return self

  def add_node(self, node):
    if node in self.adjacency_list:
      print("This node already exists")
    else: 
      self.number_of_nodes += 1
      self.adjacency_list[node] = []

  def add_edge(self, node1, node2, weight):
    if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
      print("Node does not exist")
    else:
      pair1 = [node2, int(weight)]
      pair2 = [node1, int(weight)]
      self.number_of_edges += 1
      self.adjacency_list[node1].append(pair1)
      self.adjacency_list[node2].append(pair2)
      print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA JUST MARCOS")
      print("STURULOSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

  def add_nodes(self, nodes_filepath):
    with open(nodes_filepath, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.add_node(row[0])

  def add_edges(self, edges_filepath):
    with open(edges_filepath, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.add_edge(row[0], row[1], row[2])

  def print_adjacency_list(self):
    print("Graph as Adjacency List:")
    for node in self.adjacency_list:
      print(node, " -> ", self.adjacency_list[node])

  def degree(self, node):
    return len(self.adjacency_list[node])

  def is_node_in_adjacency(node1, node2):
    for node in self.adjacency_list[node1]:
      if node2 == node[0]:
        return True
    return False

  def has_edge(self, node1, node2):
    if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
      return False
    if node1 == node2:
      return True
    return self.is_node_in_adjacency(node1, node2)

  def is_complete(self):
    return self.number_of_edges == comb(self.number_of_nodes, 2)

  def pair_from_list(self, node2, node1):
    for pair in self.adjacency_list[node1]:
      if node2 == pair[0]:
        return pair

  def remove_edge(self, node1, node2):
    if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
      print("Node does not exist")
    else:
      self.number_of_edges -= 1
      self.adjacency_list[node1].remove(self.pair_from_list(node2, node1))
      self.adjacency_list[node2].remove(self.pair_from_list(node1, node2))
