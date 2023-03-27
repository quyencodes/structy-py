"""
brute force solution:
1) initialize a set, largest_component and iteratively go through the nodes in the adjacency list
2) recursively visited edges and increment each node's count by 1 and at the top level return the total count
3) compare largest_component with total count - update if total is larger than largest_component
4) return largest_component


time - o(e)
space - o(n)

"""

def largest_component(graph):
  largest_component, visited = 0, set()
  for node in graph:
    curr = explore_components(graph, node, visited)
    if largest_component < curr:
      largest_component = curr

  return largest_component

def explore_components(graph, current, visited):
  if current in visited:
    return 0

  visited.add(current)

  count = 1
  for neighbor in graph[current]:
    count += explore_components(graph, neighbor, visited)

  return count