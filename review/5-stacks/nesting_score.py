def nesting_score(string):
  stack = [0]
  for b in string:
    if b == ']':
      curr = stack.pop()
      if curr == 0:
        stack[-1] += 1
      else:
        stack[-1] += curr * 2
    else:
      stack.append(0)

  return stack[0]

nesting_score("[[][]][]") # -> 5
"""
"[][[][]][[]]

[1, 4]



"[[][]][]"
[0, 0]

"""

