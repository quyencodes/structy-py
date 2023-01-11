def connected_components_count(graph):
  visited = set()
  count = 0
  for node in graph:
    count += explore_path(graph, node, visited)
  return count

def explore_path(graph, current, visited):
  if current in visited:
    return 0

  visited.add(current)

  for neighbor in graph[current]:
    explore_path(graph, neighbor, visited)

  return 1

# visited = {0, 8, 5, 1}

# explore_path(graph, 0, visited)
# | 0 not in visited
# | neighbors = [8, 1, 5]
# | explore_path(8) = 1
# | explore_path(1) = 1
# | explore_path(5) = 0

# explore_path(8)
# | 8 not in visited
# | neighbors = [0, 5]
# | explore_path(0) = 0
# | explore_path(5) = 1
#
# explore_path(5)
# | 5 not in visited
# | neighbors = [0, 8]
# | explore_path(0) = 0
# | explore_path(8) = 0
# | return 1