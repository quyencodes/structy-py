from collections import deque
def shortest_path(edges, node_A, node_B):
  graph = create_graph(edges)
  visited = set([node_A])

  queue = deque( [ (node_A, 0) ])
  while queue:
    current, distance = queue.popleft()

    if current == node_B:
      return distance

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(current)
        queue.append((neighbor, distance + 1))

  return -1

def create_graph(edges):
  graph = {}

  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph

# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# graph = {
#   'v': ['w', 'v'],
#   'w': ['x', 'v'],
#   'x': ['w', 'y'],
#   'y': ['x', 'z'],
#   'z': ['y', 'v'],
# }