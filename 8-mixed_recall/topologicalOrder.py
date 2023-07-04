import collections
def topological_order(graph):
  num_parents = get_num_parents(graph)
  topological_values = []

  queue = collections.deque([ child for child, parents in num_parents.items() if parents == 0 ])

  while queue:
    current = queue.popleft()
    topological_values.append(current)

    for child in graph[current]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        queue.append(child)

  return topological_values

def get_num_parents(graph):
  num_parents = { node:0 for node in graph } # c:0, a: 1, f: 2, b: 1, e: 2, d: 1

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  return num_parents

test = {
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}
print(get_num_parents(test))