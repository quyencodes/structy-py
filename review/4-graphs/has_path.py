# iterative bfs
def has_path(graph, src, dst):
  queue = [ src ]
  while queue:
    current = queue.pop(0)
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)
  return False

def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True

  return False