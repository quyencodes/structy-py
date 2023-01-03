def depth_first_print(graph, start):
  stack = [ start ]
  while stack:
    current = stack.pop()
    print(current)
    for neighbor in graph[current]:
      stack.append(neighbor)

from collections import deque
def breadth_first_print(graph, start):
  queue = deque([ start ])
  while queue:
    current = queue.popleft()
    print(current)
    for neighbor in graph[current]:
      queue.append(neighbor)

def depth_first_print_recursive(graph, current):
  print(current)
  for neighbor in graph[current]:
    depth_first_print_recursive(graph, neighbor)

graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}