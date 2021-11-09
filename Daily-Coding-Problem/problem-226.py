def create_graph(words):
  letters = set(''.join(words))
  graph = {letter: [] for letter in letters}

  for pair in zip(words, words[1:]):
    for before, after in zip(*pair):
      if before != after:
        graph[before].append(after)
        break

  return graph

from collections import deque

def visit(letter, graph, visited, order):
  visited.add(letter)

  for next_letter in graph[letter]:
    if next_letter not in visited:
      visit(next_letter, graph, visited, order)

  order.appendleft(letter)

def toposort(graph):
  visited = set()
  order = deque([])

  for letter in graph:
    if letter not in visited:
      visit(letter, graph, visited, order)

  return list(order)

def alien_letter_order(words):
  graph = create_graph(words)
  return toposort(graph)
