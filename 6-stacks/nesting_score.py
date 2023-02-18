# [] 1 point
# [nested] 2 * nested
def nesting_score(string):
  stack = [0]
  for char in string:
    if char == '[':
      stack.append(0)
    else:
      if stack[-1] == 0: # zero
        current = stack.pop()
        stack[-1] += 1
      else: # non zero
        current = stack.pop()
        val = current * 2
        stack[-1] += val

  return stack.pop()