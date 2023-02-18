def paired_parentheses(string):
  stack = []
  for s in string:
    if s.isalpha():
      continue

    if len(stack) > 0 and s == ')' and stack[-1] == '(':
      stack.pop()
    else:
      stack.append(s)

  print(stack)
  if len(stack) == 0:
    return True
  else:
    return False

print(paired_parentheses("(david)((abby))")) # -> True

