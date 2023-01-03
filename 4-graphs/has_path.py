# bfs
from collections import deque
def has_path(graph, src, dst):
  queue = deque([ src ])
  while queue:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)

  return False

# dfs
def has_path(graph, src, dst):
  stack = [ src ]
  while stack:
    current = stack.pop()
    if current == dst:
      return True

    for neighbor in graph[current]:
      stack.append(neighbor)

  return False

# recursive
def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True

  return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}