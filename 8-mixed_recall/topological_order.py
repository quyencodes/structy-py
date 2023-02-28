def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  ready = [ node for node in num_parents if num_parents[node] == 0]

  order = []
  while len(ready) > 0:
    node = ready.pop()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)

  return order

from collections import deque
def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  print(num_parents)
  ready = deque([ node for node in graph if num_parents[node] == 0 ])
  order = []

  while ready:
    node = ready.popleft()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)

  return order

topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
})

g = lambda x: x[0]
print(g([3, 1, 2]))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name('   quyen', 'hoang'))

scifi_authors = ['Issac Ashimov', 'Ray Bradbury']
print(scifi_authors.split(' '))

values = sorted(scifi_authors, key=lambda names: names.split(' ')[-1].lower())
print(values)