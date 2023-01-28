graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': [],
}

# def depth_first_print(graph, start):
#   stack = [ start ]
#   while len(stack) > 0:
#     current = stack.pop()
#     print(current)

#     for neighbor in graph[start]:
#       stack.append(neighbor)

def depth_first_print(graph, current):
  print(current)

  for neighbor in graph[current]:
    depth_first_print(graph, neighbor)

# def depth_first_print(graph):
#   visited = set()
#   for node in graph:
#     explore_graph(graph, node, visited)

# def explore_graph(graph, current, visited):

#   if current in visited:
#     return
#   visited.add(current)

#   print(current)

#   for neighbor in graph[current]:
#     explore_graph(graph, neighbor, visited)

print(depth_first_print(graph, 'a'))