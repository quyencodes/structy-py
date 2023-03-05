# s - length of the string
# n - chars in the string
# time complexity - o(n)
# space complexity - o(n)

def compress(s):
  s += '!'
  res, i, j = [], 0, 0
  while j < len(s):
    if s[i] != s[j]:
      freq = j - i
      group = s[i] if freq == 1 else str(freq) + s[i]
      res.append(group)
      i = j
    else:
      j += 1

  return ''.join(res)

"""
compress('ccaaatsss') # -> '2c3at3s'
      i
ccaaatsss!
         j
freq = 3
group = '3a'
res = [2c3a]


i = represents the beginning of the char
j = when new char is met
"""