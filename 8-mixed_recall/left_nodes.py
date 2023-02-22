class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

import collections
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lefty_nodes(root):
  lefty = []
  _lefty_nodes(root, 0, lefty)
  return lefty


def _lefty_nodes(root, level, lefty):
  if root is None:
    return

  if len(lefty) == level:
    lefty.append(root.val)

  _lefty_nodes(root.left, level+1, lefty)
  _lefty_nodes(root.right, level+1, lefty)

"""
bfs levels traversal
[[u], [t, s], [r], [q, p]]
popleft() each sublist
"""

u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')

u.left = t
u.right = s
s.right = r
r.left = q
r.right = p

#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]


def lefty_nodes(root):
  levels = levels_traversal(root)
  levels = collections.deque(levels)
  res = []
  for level in levels:
    res.append(level.pop(0))
  return res


def levels_traversal(root):
  if root is None: return []
  levels = []
  queue = collections.deque([(root, 0)])
  while queue:
    current, lvl = queue.popleft()

    if len(levels) == lvl:
      levels.append([current.val])
    else:
      levels[lvl].append(current.val)

    if current.left:
      queue.append((current.left, lvl+1))
    if current.right:
      queue.append((current.right, lvl+1))

  return levels

"""
bfs levels traversal
[[u], [t, s], [r], [q, p]]
popleft() each sublist
"""

u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')

u.left = t
u.right = s
s.right = r
r.left = q
r.right = p

#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]