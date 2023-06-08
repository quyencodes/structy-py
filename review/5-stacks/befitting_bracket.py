"""
brute force solution:
1. initialize stack to keep track of brackets
2. if closing bracket
   2a. check dictionary (key - closing bracket, value - opening bracket)
   2b. pop off stack if opening bracket is appropriate bracket
3. if opening bracket -> append to stack
4. check to see if our stack is empty

time - o(s), s being the string we are working with
space - o(s), s being the string (worse case, all closing brackets)

example:
'(){}[](())' -> True
  s
stack = []

"""

def befitting_brackets(string):
  stack = []
  closing = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  for s in string:
    if s not in closing:
      stack.append(s)
    else:
      if len(stack) == 0: return False
      if closing[s] == stack[-1]:
        stack.pop()

  return len(stack) == 0

befitting_brackets('(){}[](())')
