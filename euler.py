from graph import Graph

def is_odd(number):
  return number % 2 == 1

def number_of_odd_degrees(graph):
  odd_degrees = 0
  for node in graph.adjacency_list:
    if is_odd(graph.degree(node[0])):
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
    print('Nem Euleriano nem Semi-Euleriano')

def fleury_algorithm(graph, origin):
  # Follow edges that are not dead ends one at a time
  distance = 0
  while(graph.number_of_edges != 0):
    if graph.number_of_edges == 1:
      destiny = graph.adjacency_list[origin][0][0]
      print(origin, '->', destiny)
      distance += graph.pair_from_list(origin, destiny)[1]
      graph.remove_edge(origin, destiny)
      origin = destiny
    else:
      for possible_destiny in graph.adjacency_list[origin]:
        if graph.degree(possible_destiny[0]) != 1:
          destiny = possible_destiny[0]
          print(origin, '->', destiny)
          distance += graph.pair_from_list(origin, destiny)[1]
          graph.remove_edge(origin, destiny)
          origin = destiny
          break
  print('Distância', distance)

def print_cycle(graph):
  g = graph
  fleury_algorithm(g, origin = list(g.adjacency_list)[0][0])

def print_path(graph):
  g = graph
  origin = None

  for node in g.adjacency_list:
    if is_odd(g.degree(node[0])):
      origin = node
      break

  fleury_algorithm(g, origin)

print('Grafo 1:')
evaluate_eulerity(Graph().from_filepaths('nodes.csv', 'edges1.csv'))
print('')

print('Grafo 2:')
evaluate_eulerity(Graph().from_filepaths('nodes.csv', 'edges2.csv'))
print('')

print('Grafo 3:')
evaluate_eulerity(Graph().from_filepaths('nodes.csv', 'edges3.csv'))
print('')

print('Grafo 4:')
evaluate_eulerity(Graph().from_filepaths('nodes.csv', 'edges4.csv'))
print('')
