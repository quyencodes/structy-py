def can_color(graph):
  coloring = {}
  for node in graph:
    if node not in coloring and not validate(graph, node, coloring, False):
      return False
  return True

def validate(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color

  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False

  return True

"""
red = x
blue = y
"""