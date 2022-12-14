# input - string formatted in multiple groups
# output - uncompressed version of the string where each 'char' of a group is repeated n times consecutively
# constraints - none
# edge cases - not well formmatted data - but none for now

def uncompress(s):
  # initialize variables
  # store all the groups of chars and n
  result = ''
  # keep track of n (number of instances of char)
  n = ''
  # if value is a number
  nums = '1234567890'

  # iterate over the string
  for value in s:
    # if the element is a string
    if value in nums:
      n += value
    else:
      result += (int(n) * value)
      # get the num and multiply it by the string, += to result
      n = ''


  # return result
  return result

print(uncompress("2c3a1t"))

# n = # of groups
# m = max number for any group
# time - o(n*m)
# space - o(n*m)