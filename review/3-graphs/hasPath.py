# time o(e), where e is the number of edges
# space - o(n), where n is the number of nodes

def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True

  return False

from collections import deque
def has_path(graph, src, dst):
  queue = deque([src])

  while queue:
    current = queue.popleft()

    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)

  return False