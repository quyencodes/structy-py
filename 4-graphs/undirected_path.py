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
    if has_path(graph, neighbor, dst, visited) == True:
      return True

  return False

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

from collections import deque
def undirected_path(edges, node_A, node_B):
  queue = deque([ node_A ])
  graph = create_graph(edges)
  visited = set()
  while queue:
    current = queue.popleft()
    if current == node_B:
      return True

    visited.add(current)

    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append(neighbor)

  return False