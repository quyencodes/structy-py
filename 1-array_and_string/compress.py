# input - uncompressed version of a string
# output - compressed version of the string compressed by number of occurence and character
# constraints - none
# edge cases - if there is no number

def compress(s):
  # because while loop logic only enters else case when streak of chars terminates
  s += '!'
  result = ''
  i = 0
  j = 0

  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      if len(s[i:j]) == 1:
        result += s[i]
      else:
        result += str(len(s[i:j])) + s[i]
      i = j

  return result

# test case 1
print(compress('ccaaatsss'))