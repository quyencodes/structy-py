def connected_components_count(graph):
  visited = set()
  count = 0
  for node in graph:
    if explore_nodes(graph, node, visited) == True:
      count += 1
  return count

def explore_nodes(graph, current, visited):
  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    explore_nodes(graph, neighbor, visited)

  return True