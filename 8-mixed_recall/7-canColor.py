def can_color(graph):
  colors = {} # node - color
  color_code = True # even - red, odd - blue
  for node in graph:
    if node not in colors and _can_color(graph, node, colors, not color_code) == False:
      return False

  return True

def _can_color(graph, current, colors, code):
  if current in colors and colors[current] != code:
    return False
  elif current in colors and colors[current] == code:
    return True

  colors[current] = code

  for neighbor in graph[current]:
    if _can_color(graph, neighbor, colors, not code) == False:
      return False

  return True


def detect_cycle(graph):
  visited = set()
  visiting = set()
  for node in graph:
    if has_cycle(graph, node, visiting, visited):
      return True

  return False

def has_cycle(graph, current, visiting, visited):
  if current in visited:
    return False

  if current in visiting:
    return True

  visiting.add(current)

  for neighbor in graph[current]:
    if has_cycle(graph, neighbor, visiting, visited):
      return True

  visiting.remove(current)
  visited.add(current)
  return False


