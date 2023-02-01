def prereqs_possible(num_courses, prereqs):
  visiting = set()
  visited = set()
  graph = create_graph(num_courses, prereqs)

  for node in graph:
    if explore_schedule(graph, node, visiting, visited):
      return False
    visiting = set()

  return True

def explore_schedule(graph, current, visiting, visited):
  if current in visited:
    return False

  if current in visiting:
    return True
  visiting.add(current)

  for neighbor in graph[current]:
    if explore_schedule(graph, neighbor, visiting, visited):
      return True

  # visiting.remove(current)
  visited.add(current)
  return False


def create_graph(num_courses, prereqs):
  graph = {}

  for courses in range(0, num_courses):
    graph[courses] = []

  for prereq in prereqs:
    a, b = prereq
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
prereqs_possible(numCourses, prereqs) # -> True