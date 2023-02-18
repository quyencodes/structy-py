def befitting_brackets(string):
  stack = []
  for s in string:
    if len(stack) > 0 and s == ')' and stack[-1] == '(':
      stack.pop()
    elif len(stack) > 0 and s == '}' and stack[-1] == '{':
      stack.pop()
    elif len(stack) > 0 and s == ']' and stack[-1] == '[':
      stack.pop()
    else:
      stack.append(s)

  if len(stack) == 0:
    return True
  else:
    return False

print(befitting_brackets('(){}[](())')) # -> True

