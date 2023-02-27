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
