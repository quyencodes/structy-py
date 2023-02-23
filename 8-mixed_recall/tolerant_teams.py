def tolerant_teams(rivalries):
  graph = build_graph(rivalries)
  coloring = {}
  for node in graph:
    if node not in coloring and not pick_teams(graph, node, coloring, False):
      return False
  return True

def pick_teams(graph, node, coloring, current_color):
  if node in coloring:
    return coloring[node] == current_color

  coloring[node] = current_color

  for neighbor in graph[node]:
    if not pick_teams(graph, neighbor, coloring, not current_color):
      return False

  return True

def build_graph(edges):
  graph = {}
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph
"""
{
  philip: ['seb']
  seb: ['philip']

}

"""