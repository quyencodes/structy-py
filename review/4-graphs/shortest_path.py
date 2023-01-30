# input - edge list, two nodes - start node and end node
# output - the shortest path between start and end
# constraints - none
# edge cases - none

def shortest_path(edges, node_A, node_B):
  # build a graph
  visited = set([node_A])
  graph = build_graph(edges)
  # bfs and will keep track of what distance
  queue = [(node_A, 0)]
  while queue:
    current = queue.pop(0)
    node, distance = current

    if node == node_B:
      return distance

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append((neighbor, distance + 1))
        visited.add(neighbor)

  # return -1
  return -1

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