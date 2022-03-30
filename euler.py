from graph import Graph
import copy

def is_odd(number):
  return number % 2 == 1

def number_of_odd_degrees(graph):
  odd_degrees = 0
  for node in graph.nodes:
    if is_odd(graph.nodes[node].degree()):
      odd_degrees += 1
  return odd_degrees

def evaluate_eulerity(graph):
  odd_degrees = number_of_odd_degrees(graph)
  if odd_degrees == 0:
    print('Grafo é Euleriano')
    print_cycle(graph)
  elif odd_degrees == 2:
    print('Grafo é Semi-Euleriano')
    print_path(graph)
  else:
    print('Grafo é nem Euleriano nem Semi-Euleriano')

def is_final_edge(graph, node):
  return graph.nodes[node].degree() == 1

def is_not_bridge(graph, origin, destiny):
  graph_copy = copy.deepcopy(graph)
  
  visited_before = graph_copy.dfs_count_from_node(origin)
  
  graph_copy.remove_edge(origin, destiny)
  graph_copy.reset_visited_nodes()
  visited_after = graph_copy.dfs_count_from_node(origin)
  
  return visited_before == visited_after

def fleury_algorithm(graph, origin):
  distance = 0
  while(graph.number_of_edges != 0):
    for possible_destiny in graph.nodes[origin].edges:
      if is_final_edge(graph, origin) or is_not_bridge(graph, origin, possible_destiny):
        destiny = possible_destiny
        print(origin, '->', destiny)
        distance += graph.nodes[origin].edges[destiny].weight
        graph.remove_edge(origin, destiny)
        origin = destiny
        break
  print('Distância', distance)

def print_cycle(graph):
  graph_copy = copy.deepcopy(graph)
  fleury_algorithm(graph_copy, origin = list(graph_copy.nodes)[0])

def origin_of_path(graph):
  for node in graph.nodes:
    if is_odd(graph.nodes[node].degree()):
      return node

def print_path(graph):
  graph_copy = copy.deepcopy(graph)
  fleury_algorithm(graph_copy, origin = origin_of_path(graph_copy))

graph_number = 0

def graph_analysis(nodes_filepath, edges_filepath):
  global graph_number
  graph_number += 1
  print('Grafo', graph_number)
  graph = Graph(nodes_filepath, edges_filepath)
  graph.print_graph()
  print()

  evaluate_eulerity(graph)
  print()

graph_analysis('nodes.csv', 'edges1.csv')
graph_analysis('nodes.csv', 'edges2.csv')
graph_analysis('nodes.csv', 'edges3.csv')
graph_analysis('nodes.csv', 'edges4.csv')
graph_analysis('nodes5.csv', 'edges5.csv')
