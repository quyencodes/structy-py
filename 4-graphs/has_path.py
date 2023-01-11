# dfs
def has_path(graph, src, dst):
  stack = [src]
  while stack:
    current = stack.pop()
    if current == dst:
      return True

    for neighbor in graph[current]:
      stack.append(neighbor)

  return False

from collections import deque
# bfs
def has_path(graph, src, dst):
  queue = deque([src])
  while queue:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)

  return False

# recursive case
def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True

  return False

# recursive case
def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False
  visited.add(src)

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, set()) == True:
      return True

  return False
