from collections import deque
def shortest_path(edges, node_A, node_B):
  visited = set()
  # create graph
  graph = create_graph(edges)

  distance = 0
  queue = deque([ (node_A, distance) ])
  while queue:
    current = queue.popleft()
    node, count = current

    if node == node_B:
      return count

    visited.add(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append((neighbor, count + 1))

  return -1

# queue = [('z', 2), ('w', 2), ('x', 3), ('z', 3)]
# current = ('z', 2)
# visited = {'w', 'x', 'v', 'y'}
# node = 'z', count = 2
# 'z' == 'z' RETURN COUNT

# ('z', 2), ('w', 2)

def create_graph(edges):
  adjacency_list = {}
  for edge in edges:
    a, b = edge
    if a not in adjacency_list:
      adjacency_list[a] = []
    if b not in adjacency_list:
      adjacency_list[b] = []

    adjacency_list[a].append(b)
    adjacency_list[b].append(a)

  return adjacency_list

edges = [
  ['w', 'x'],
  ['y', 'x'],
  ['z', 'y'],
  ['z', 'v'],
  ['v', 'w'],
]

graph = {
  'w': ['x', 'v'],
  'y': ['x', 'z'],
  'x': ['w', 'y'],
  'z': ['y', 'v'],
  'v': ['z', 'w'],
}