def decompress_braces(string):
  nums_char = '123456789'
  stack = []
  for char in string:
    if char in nums_char:
      stack.append(int(char))
    else:
      if char == '}':
        # popping subroutine
        segment = ''
        while not isinstance(stack[-1], int):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)

  return ''.join(stack)



from collections import deque
def decompress_braces(string):
  stack = []
  for char in string:
    if char == '}':
      # iterate through the stack until i hit a number
      i = len(stack) - 1
      res = deque([])
      num = stack[i] # q
      while num.isalpha():
        letter = stack.pop() # remove it
        res.appendleft(letter) # record it
        i-=1
        num = stack[i]

      stack.remove(num)
      temp = ''.join(res)
      print(temp)
      stack.append(int(num) * temp)
    else:
      if char != '{':
        stack.append(char)

  print(stack)
  return ''.join(stack)

decompress_braces("2{q}3{tu}v")