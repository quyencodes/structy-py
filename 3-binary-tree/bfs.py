from collections import deque

# iterative solution
def breadth_first_values(root):
  if root is None:
    return []

  queue = deque([ root ])
  values = []

  while queue:
    current = deque.popleft()
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return values

# iterative solution
def breadth_first_values(root):
  if root is None:
    return []

  queue = [ root ]
  values = []

  while queue:
    current = queue.pop(0)
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return values