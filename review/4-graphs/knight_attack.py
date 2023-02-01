from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  visited = set([(kr, kc)])
  queue = deque([(kr, kc, 0)])
  while queue:
    current = queue.popleft()
    row, col, distance = current

    if (row, col) == (pr, pc):
      return distance

    valid_moves = find_valid_moves(n, row, col)
    for move in valid_moves:
      neighbor_row, neighbor_col = move
      if move not in visited:
        queue.append((neighbor_row, neighbor_col, distance + 1))
        visited.add((neighbor_row, neighbor_col))
  return -1

def find_valid_moves(n, kr, kc):
  valid_positions = []
  deltas = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

  for delta in deltas:
    delta_row, delta_col = delta
    neighbor_row = delta_row + kr
    neighbor_col = delta_col + kc
    if is_inbounds(n, neighbor_row, neighbor_col):
      valid_positions.append((neighbor_row, neighbor_col))

  return valid_positions

def is_inbounds(n, r, c):
  row_inbounds = 0 <= r < n
  col_inbounds = 0 <= c < n
  return row_inbounds and col_inbounds