# white, grey, black algorithm
def prereqs_possible(num_courses, prereqs):
  visiting = set()
  visited = set()
  graph = create_graph(prereqs)
  for node in graph:
    if explore(graph, node, visiting, visited) == False:
      return False

  return True

def explore(graph, current, visiting, visited):
  if current in visited:
    return

  if current in visiting:
    return False

  visiting.add(current)

  for neighbor in graph[current]:
    if explore(graph, neighbor, visiting, visited) == False:
      return False

  visiting.remove(current)
  visited.add(current)
  return True

def create_graph(edges):
  graph = {}
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)

  return graph

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs)