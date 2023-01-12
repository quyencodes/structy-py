def largest_component(graph):
  visited = set()
  largest = 0
  for node in graph:
    size = explore(graph, node, visited)
    if largest < size:
      largest = size

  return largest

def explore(graph, current, visited):
  if current in visited:
    return 0

  visited.add(current)

  count = 1
  for neighbor in graph[current]:
    count += explore(graph, neighbor, visited)

  return count

# visited = {0, 8, 5, 1}

# explore(graph, 0, visited)
# 0 not in visited
# count = 1
# explore(graph, 8, visited) = 2
# explore(graph, 1, visited) = 1
# explore(graph, 5, visited) = 0
# return 4

# explore(graph, 8, visited) = 2
# 8 not in visited
# count = 1
# explore(graph, 0, visited) = 0
# explore(graph, 5, visited) = 1
# return 2

# explore(graph, 5, visited)
# 5 not in visited
# explore(graph, 0, visited) = 0
# explore(graph, 8, visited) = 0
# return 1

