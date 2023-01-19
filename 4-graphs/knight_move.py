from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  visited.add((kr, kc))
  queue = deque([ (kr, kc, 0) ])
  while queue:
    row, col, moves = queue.popleft()

    if (row, col) == (pr, pc):
      return moves

    valid_positions = knight_move(row, col, n)
    # pos = (row, col)
    # visited.add(pos)

    for position in valid_positions:
      knight_move_row, knight_move_col = position

      if position not in visited:
        visited.add(position)
        queue.append((knight_move_row, knight_move_col, moves + 1))

  return None

def knight_move(row, col, n):
    valid_positions = []
    deltas = [
      (row-2, col-1), # knight top left
      (row-1, col-2), # knight inner top left
      (row+1, col-2), # knight inner bottom left
      (row+2, col-1), # knight bottom left
      (row-2, col+1), # knight top right
      (row-1, col+2), # knight inner top right
      (row+1, col+2), # knight inner bottom right
      (row+2, col+1), # knight bottom right
    ]

    for delta in deltas:
      knight_move_row, knight_move_col = delta
      if 0 <= knight_move_row < n and 0 <= knight_move_col < n:
        valid_positions.append(delta)

    return valid_positions


# attempt 2
from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  queue = deque([ (kr, kc, 0) ])
  while queue:
    row, col, moves = queue.popleft()

    if (row, col) == (pr, pc):
      return moves

    pos = (row, col)
    visited.add(pos)

    valid_positions = knight_move(row, col, n)

    for position in valid_positions:
      knight_move_row, knight_move_col = position

      if position not in visited:
        queue.append((knight_move_row, knight_move_col, moves + 1))

  return None

def knight_move(row, col, n):
    valid_positions = []
    deltas = [
      (row-2, col-1), # knight top left
      (row-1, col-2), # knight inner top left
      (row+1, col-2), # knight inner bottom left
      (row+2, col-1), # knight bottom left
      (row-2, col+1), # knight top right
      (row-1, col+2), # knight inner top right
      (row+1, col+2), # knight inner bottom right
      (row+2, col+1), # knight bottom right
    ]

    for delta in deltas:
      knight_move_row, knight_move_col = delta
      if 0 <= knight_move_row < n and 0 <= knight_move_col < n:
        valid_positions.append(delta)

    return valid_positions


# attempt 1
from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  board = create_board(n, pr, pc)
  visited = set()
  queue = deque([ (kr, kc, 0) ])
  while queue:
    row, col, moves = queue.popleft()

    if board[row][col] == 'p':
      return moves

    pos = (row, col)
    visited.add(pos)

    deltas = [
      (-2, -1), # knight top left
      (-1, -2), # knight inner top left
      (1, -2), # knight inner bottom left
      (2, -1), # knight bottom left
      (-2, 1), # knight top right
      (-1, 2), # knight inner top right
      (1, 2), # knight inner bottom right
      (2, 1), # knight bottom right
    ]

    for delta in deltas:
      delta_row, delta_col = delta
      knight_move_row = row + delta_row
      knight_move_col = col + delta_col

      if is_inbounds(knight_move_row, knight_move_col, n) and (knight_move_row, knight_move_col) not in visited:
        queue.append((knight_move_row, knight_move_col, moves + 1))

  return None



def is_inbounds(row, col, n):
  row_inbounds = 0 <= row < n
  col_inbounds = 0 <= col < n
  return row_inbounds and col_inbounds

def create_board(n, pr, pc):
  board = []
  for row in range(0, n):
    board.append(list(n*'x'))

  board[pr][pc] = 'p'

  return board




[
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'p', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]