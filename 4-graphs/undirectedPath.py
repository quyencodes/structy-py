def undirected_path(edges, node_A, node_B):
  visited = set()
  graph = create_graph(edges)
  return has_path(graph, node_A, node_B, visited)


def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False
  visited.add(src)

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited):
      return True

  return False


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


"""
i - j
|
k - m
|
l

o - n
"""
