def longest_path(graph):
  distances = {}
  # store terminal nodes
  for node in graph:
    if len(graph[node]) == 0:
      distances[node] = 0

  print(distances)

  for node in graph:
    if node not in distances:
      explore_nodes(graph, node, distances)

  return max(distances.values())

def explore_nodes(graph, current, distances):
  # if its in there
  if current in distances:
    return distances[current]

  largest = 0
  for neighbor in graph[current]:
    attempt = explore_nodes(graph, neighbor, distances)
    if attempt > largest:
      largest = attempt

  distances[current] = 1 + largest
  return distances[current]

