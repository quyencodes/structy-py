# longest path question
def semesters_required(num_courses, prereqs):
  schedule = {}
  graph = build_graph(num_courses, prereqs)
  print(graph)

  # find terminal nodes
  for course in graph:
    if len(graph[course]) == 0:
      schedule[course] = 1

  for node in graph:
    if node not in schedule:
      explore(graph, node, schedule)

  return max(schedule.values())

def explore(graph, current, schedule):
  if current in schedule:
    return schedule[current]

  semester = 0
  for neighbor in graph[current]:
    print('before error', neighbor)
    attempt = explore(graph, neighbor, schedule)
    print('after error', attempt)
    if attempt > semester:
      semester = attempt

  schedule[current] = 1 + semester
  return schedule[current]

def build_graph(num_courses, edges):
  graph = {}
  for key in range(num_courses):
    graph[key] = []

  for edge in edges:
    a, b = edge
    graph[a].append(b)

  return graph

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs) # -> 3