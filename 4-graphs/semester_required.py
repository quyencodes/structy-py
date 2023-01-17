def semesters_required(num_courses, prereqs):
  schedule = {}
  graph = create_graph(prereqs)

  # find terminal nodes
  for node in graph:
    if len(graph[node]) == 0:
      schedule[node] = 1

  # traverse the graph
  for node in graph:
    explore(graph, node, schedule)

  try:
    return max(schedule.values())
  except:
    return 1

def explore(graph, node, schedule):
  if node in schedule:
    return schedule[node]

  index = 0
  for neighbor in graph[node]:
    attempt = explore(graph, neighbor, schedule)
    if index < attempt:
      index = attempt

  schedule[node] = 1 + index
  return schedule[node]

def create_graph(edge_list):
  graph = {}
  for edge in edge_list:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)

  return graph

graph = {
  1: [2],
  2: [4],
  3: [5],
  0: [5],
  4: [],
  5: [],
}