def tree_levels(root):
  if root is None: return []

  levels = []
  queue = [ (root, 0) ]
  while queue:
    current = queue.pop(0)
    node, level = current

    if len(levels) == level:
      levels.append([node.val])
    else:
      levels[level].append(node.val)

    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))

  return levels