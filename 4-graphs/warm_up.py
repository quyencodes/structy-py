def depth_first_print(graph, start):
  stack = [ start ]
  while stack is not None:
    current = stack.pop()
    print(current)
    for neighbor in graph[current]:
      stack.append(neighbor)

def depth_first_print(graph, current):
  print(current)
  for neighbor in graph[current]:
    depth_first_print(graph, current)

from collections import deque
def breadth_first_print(graph, start):
  queue = deque([start])
  while queue is not None:
    current = queue.popleft()
    for neighbor in graph[current]:
      queue.append(neighbor)

graph = {
  "a": ['b', 'c'],
  "b": ['d'],
  "c": ['e'],
  "d": ['f'],
  "e": [],
  "f": [],
}

depth_first_print(graph)