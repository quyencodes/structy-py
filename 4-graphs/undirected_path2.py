def undirected_path(edges, node_A, node_B):
  graph = create_graph(edges)

  def pathsolver(graph, src, dst, visited):
    if src == dst:
      return True

    visited.add(src)

    for neighbor in graph[src]:
      if pathsolver(graph, neighbor, dst, visited) == True:
        return True

    return False

  return pathsolver(graph, node_A, node_B, set())

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