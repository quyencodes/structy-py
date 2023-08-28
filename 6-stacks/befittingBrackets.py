def befitting_brackets(string):
  stack = []
  brackets = {
    '}': '{',
    ')': '(',
    ']': '['
  }

  for s in string:
    if s in brackets:
      if stack and stack[-1] == brackets[s]:
        stack.pop()
      else:
        return False
    else:
      stack.append(s)

  return len(stack) == 0
