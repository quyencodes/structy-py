def has_cycle(graph):
  visiting, visited = set(), set()
  for node in graph:
    if detect_cycle(graph, node, visiting, visited):
      return True

  return False

def detect_cycle(graph, current, visiting, visited):
  if current in visited:
    return False

  if current in visiting:
    return True

  visiting.add(current)

  for neighbor in graph[current]:
    if detect_cycle(graph, neighbor, visiting, visited):
      return True

  visiting.remove(current)
  visited.add(current)

  return False
