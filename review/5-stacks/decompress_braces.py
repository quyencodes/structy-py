"""
"2{q}3{tu}v"
qqtututuv

"2{y3{o}}s"
[2, y, 3, o]
[yooo, yooo, s]

1. initialize my stack
2. if its not a closing curly braces -> append to stack
3. if a closing braces:
   3a. if stack and iterate from the back of the stack until we see a number
   3b. grab number, the words, multiply together
   3c. add back to the stack
end. return ''.join(stack)

"""
import collections
def decompress_braces(string):
  stack = []
  nums = '0123456789'

  for c in string:
    if c == '}':
      temp = collections.deque([])
      while stack and stack[-1] not in nums:
        temp.appendleft(stack.pop())
      num = stack.pop()
      stack.append(int(num) * ''.join(temp))
    elif is_alnum(c):
      stack.append(c)

  return ''.join(stack)

"""
"2{y3{o}}s"
stack = [yoooyooos], last_element = '3'
temp = []
"""

def is_alnum(char):
  return ord('1') <= ord(char) <= ord('9') or ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z')