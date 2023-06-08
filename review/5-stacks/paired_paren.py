"""
realizations:
1) at all times, our stack will only have opening parentheses,
so we don't have to check if our last element is '('
2) if we are at a closing bracket and our stack is empty (count = -1),
we can return False immediately
"""


"""
brute force solution:
1. initialize a stack
2. if opening parenthesis -> add to stack
3. if closing parenthesis -> pop off last item from stack
4. if we're looking at a character, can just simply continue
5. return len(stack) == 0

time - o(s), s being the string input
space - o(s), worse case: all closing parentheses

optimal solution:
time - o(s), s being the string input
space - o(1), using a count instead
"""

"""
example:
"))()"
 s

stack = []

"""

def paired_parentheses(string):
  count = 0
  for s in string:
    if is_alpha(s): continue
    count += 1 if s == '(' else -1
    if count < 0: return False

  return count == 0

def is_alpha(char):
  return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z')



def _paired_parentheses(string):
  stack = []
  for s in string:
    if s == '(':
      stack.append(s)
    elif s == ')':
      if len(stack) == 0: return False
      stack.pop()

  return len(stack) == 0

def __paired_parentheses(string):
  stack = []
  for s in string:
    if len(stack) == 0:
      stack.append(s)
    else:
      if s == '(':
        stack.append(s)
      elif s == ')':
        last_element = stack[-1]
        if last_element == '(':
          stack.pop()
        else:
          stack.append(s)

  return len(stack) == 0

