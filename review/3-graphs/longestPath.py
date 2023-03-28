"""
brute force solution:
depth first search
1) map = {node: distance}
2) iteratively go through each node
3) return max(map.values())

"""

def longest_path(graph):
  # find terminal nodes (distance of 0)
  memo = {}
  for node in graph:
    if len(graph[node]) == 0:
      memo[node] = 0

  for node in graph:
    # recursively go through each node and try to find distance
    explore_nodes(graph, node, memo)

  return max(memo.values())

def explore_nodes(graph, current, memo):
  if current in memo:
    return memo[current]

  max_path = 0
  for neighbor in graph[current]:
    attempt = explore_nodes(graph, neighbor, memo) # 0
    if max_path < attempt:
      max_path = attempt

  memo[current] = 1 + max_path
  return memo[current]