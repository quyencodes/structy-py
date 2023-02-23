class Solution:
  def rare_routing(self, n, roads):
    visited = set()
    graph = self.build_graph(n, roads)
    # print(graph)
    valid = self.unique_path(graph, 0, visited, None)
    return valid and len(visited) == n

  def unique_path(self, graph, node, visited, last_node):
    if node in visited:
      return False

    visited.add(node) # 0, 1

    for neighbor in graph[node]:
      if neighbor != last_node and not self.unique_path(graph, neighbor, visited, node):
        return False

    return True

  def build_graph(self, n, edges):
    graph = {}

    for i in range(n):
      graph[i] = []

    for edge in edges:
      a, b = edge
      graph[a].append(b)
      graph[b].append(a)

    return graph

soln = Solution()
print(soln.rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3)
])) # -> True)