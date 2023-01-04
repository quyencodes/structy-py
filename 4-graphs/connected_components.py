def connected_components_count(graph):
  visited = set()
  count = 0

  def connectedhelper(graph, current, visited):
    if current in visited:
      return False

    visited.add(current)

    for neighbor in graph[current]:
      connectedhelper(graph, neighbor, visited)

    return True

  for node in graph:
    if connectedhelper(graph, node, visited) == True:
      count += 1

  return count
