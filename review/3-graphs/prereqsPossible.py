def prereqs_possible(num_courses, prereqs):
  graph = create_graph(num_courses, prereqs)
  visiting, visited = set(), set()
  for node in graph:
    if whitegreyblack(graph, node, visiting, visited):
      return False

  return True

def whitegreyblack(graph, current, visiting, visited):
  # check if black
  if current in visited:
    return False

  # check if grey
  if current in visiting:
    return True

  visiting.add(current)

  for neighbor in graph[current]:
    if whitegreyblack(graph, neighbor, visiting, visited):
      return True

  visiting.remove(current)
  visited.add(current)
  return False

def create_graph(num_courses, prereqs):
  graph = {}

  for course in range(0, num_courses):
    graph[course] = []

  for prereq in prereqs:
    course_a, course_b = prereq
    graph[course_a].append(course_b)

  return graph