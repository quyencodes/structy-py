def has_cycle(graph):
  visiting = set()
  visited = set()
  for node in graph:
    if cycle_detect(graph, node, visiting, visited) == True:
      return True

  return False

def cycle_detect(graph, current, visiting, visited):
  if current in visited:
    return False

  if current in visiting:
    return True
  visiting.add(current)

  for neighbor in graph[current]:
    if cycle_detect(graph, neighbor, visiting, visited):
      return True

  visiting.remove(current)
  visited.add(current)

  return False
