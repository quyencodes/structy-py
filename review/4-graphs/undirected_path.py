def undirected_path(edges, node_A, node_B):
  visited = set()
  graph = build_graph(edges)
  return explore(graph, node_A, node_B, visited)

def explore(graph, current, dst, visited):
  if current == dst:
    return True

  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    if explore(graph, neighbor, dst, visited) == True:
      return True

  return False

def build_graph(edges):
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

"""
  {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i']
    ...
  },
"""