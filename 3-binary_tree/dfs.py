# iterative approach
def depth_first_search(root):
  if root is None:
    return []

  # stack will store instances of Node
  stack = [ root ]
  values = []

  while stack:
    # removes last element of the array
    current = stack.pop()
    values.append(current.val)

    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)

  return values

# recursive solution
def depth_first_search(root):
  if root is None:
    return []

  left_values = depth_first_search(root.left)
  right_values = depth_first_search(root.right)
  return [root.val, *left_values, *right_values]