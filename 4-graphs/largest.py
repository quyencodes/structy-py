def largest_component(graph):
  visited = set()
  max_streak = 0

  def explore_size(graph, current, visited):
    if current in visited:
      return 0

    visited.add(current)
    size = 1

    for neighbor in graph[current]:
      size += explore_size(graph, neighbor, visited)

    return size

  for node in graph:
    size = explore_size(graph, node, visited)
    if max_streak < size:
      max_streak = size

  return max_streak