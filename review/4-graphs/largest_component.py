def largest_component(graph):
  # initialize set to avoid cycles
  visited = set()
  # initialize largest component variable
  largest_component = 0
  # iterate through all the nodes in the graph
  for node in graph:
    # store count
    size = explore_nodes(graph, node, visited)
    if size > largest_component:
      largest_component = size
  return largest_component

def explore_nodes(graph, current, visited):
  if current in visited:
    return 0

  visited.add(current)

  count = 1
  for neighbor in graph[current]:
    count += explore_nodes(graph, neighbor, visited)

  return count