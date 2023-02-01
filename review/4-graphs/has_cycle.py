def has_cycle(graph):
  # white-grey-black algorithm
  # white = unvisited nodes, grey = visiting nodes, black = fully visited
  visiting = set()
  visited = set()
  for node in graph:
    if detect_cycles(graph, node, visiting, visited):
      return True
    visiting = set()

  return False

def detect_cycles(graph, current, visiting, visited):
  if current in visited:
    return False

  if current in visiting:
    return True
  visiting.add(current)

  for neighbor in graph[current]:
    if detect_cycles(graph, neighbor, visiting, visited):
      return True

  # switch move from visiting to visited
  # visiting.remove(current)
  visited.add(current)
  return False

# visiting =
# visited = a, b, c, d

# a -> b -> c -> d