# input - string (groups of letters)
# output - compressed version of the string number + letter
# constraints - none
# edge case - if its 1 then just print the number

def compress(s):
  s += '!'
  i = 0
  j = 0
  result = ''
  while j < len(s):
    if s[i] != s[j]:
      freq = len(s[i:j])
      if freq == 1:
        result += s[i]
      else:
        result += str(freq) + s[i]
      i = j

    # move along j
    j += 1

  return result

#   i
# ccaaatsss!
#      j

# if s[i] != s[j]
# from len(s[i:j]) == 1
# add to result just the letter s[i]
# else > 1
# add len(s[i:j]) to result and the letter s[i]

# more optimal solution
def compress(s):
  s += '!'
  i = 0
  j = 0
  result = []
  while j < len(s):
    if s[i] != s[j]:
      freq = len(s[i:j])
      if freq == 1:
        result.append(s[i])
      else:
        result.append(str(freq) + s[i])
      i = j

    # move along j
    j += 1

  return ''.join(result)