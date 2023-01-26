def tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  return tree_includes(root.left, target) or tree_includes(root.right, target)

def tree_includes(root, target):
  if root is None: return False
  queue = [ root ]
  while queue:
    current = queue.pop(0)
    if current.val == target:
      return True

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return False