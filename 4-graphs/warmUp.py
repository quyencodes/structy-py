from collections import deque


def depth_first_print(graph, src):
  stack = [src]

  while stack:
    current = stack.pop()
    print(current)

    for neighbor in graph[current]:
      stack.append(neighbor)

  return


def _depth_first_print(graph, current):
  print(current)

  for neighbor in graph[current]:
    _depth_first_print(graph, neighbor)


def breadth_first_print(graph, src):
  q = deque([src])

  while q:
    current = q.popleft()
    print(current)

    for neighbor in graph[current]:
      q.append(neighbor)

  return 'done'


graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

# a -> b -> d -> f
# |
# v
# c -> e
#
#
