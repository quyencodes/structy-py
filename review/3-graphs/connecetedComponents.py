"""
brute force solution:
1) intialize set and count, going through the entire adjacency list iteratively
2) depth first search the components recursively
3) visit all the nodes of a connected component, add the components to a set (visited) and return some boolean data
4) increment count
5) return count
n represents our nodes in our list
e represents the connection between two nodes
time - o(e)
space - o(n)
"""

def connected_components_count(graph):
  count, visited = 0, set()
  for node in graph:
    if node not in visited and explore_components(graph, node, visited):
      count += 1
  return count

def explore_components(graph, current, visited):
  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    explore_components(graph, neighbor, visited)

  return True