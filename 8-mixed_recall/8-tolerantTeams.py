"""
get_teams helper function

"""

def tolerant_teams(rivalries):
  graph = get_teams(rivalries)
  teams = {}
  team_code = True
  for player in graph:
    team_code = not team_code
    if player not in teams and not assign_teams(graph, player, teams, team_code):
      return False

  return True

def assign_teams(graph, current, teams, team_code):
  if current in teams:
    return team_code == teams[current]

  teams[current] = team_code
  for player in graph[current]:
    if assign_teams(graph, player, teams, not team_code) == False:
      return False

  return True

def get_teams(edges):
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