"""
time - o(e), where e represents the edges
space - o(n), where n represents the nodes
"""

def semesters_required(num_courses, prereqs):
  graph = create_graph(num_courses, prereqs)
  schedule = {}

  for course in graph:
    if len(graph[course]) == 0:
      schedule[course] = 1

  for course in graph:
    explore_schedule(graph, course, schedule)

  return max(schedule.values())

def explore_schedule(graph, current, schedule):
  if current in schedule:
    return schedule[current]

  num_semesters = 0
  for neighbor in graph[current]:
    cumulative_semesters = explore_schedule(graph, neighbor, schedule)
    if num_semesters < cumulative_semesters:
      num_semesters = cumulative_semesters

  schedule[current] = 1 + num_semesters
  return schedule[current]

def create_graph(num_courses, prereqs):
  graph = {}

  for n in range(0, num_courses):
    graph[n] = []

  for prereq in prereqs:
    course_a, course_b = prereq

    graph[course_a].append(course_b)

  return graph