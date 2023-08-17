def longest_path(graph):
  distances = {}

  for node in graph:
    attempt = dfs(graph, node, distances)

  return max(distances.values())


def dfs(graph, current, distances):
  if len(graph[current]) == 0:
    distances[current] = 0
    return 0

  if current in distances:
    return distances[current]

  edges = 0
  for neighbor in graph[current]:
    attempt = dfs(graph, neighbor, distances)
    if edges < attempt:
      edges = attempt

  distances[current] = 1 + edges
  return distances[current]
