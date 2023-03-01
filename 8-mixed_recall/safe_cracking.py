def safe_cracking(hints):
  graph = build_graph(hints)

  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  # print(num_parents)
  ready = [ node for node in num_parents if num_parents[node] == 0 ]
  # print(ready)
  output = []
  while ready:
    current = ready.pop()
    output.append(str(current))

    for child in graph[current]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)

  print(output)
  return ''.join(output)

def build_graph(edges):
  graph = {}

  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
  return graph

print(safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
])) # -> '718'