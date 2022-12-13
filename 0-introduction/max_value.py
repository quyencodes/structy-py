# Input - array of numbers
# Output - largest number in the array
# Constraints - none
# Edge cases - negative numbers, empty inputs

import math

def max_value(nums):
  max_num = -math.inf
  for num in nums:
    if max_num <= num:
      max_num = num
  return max_num

# n = length of list
# time - linear o(n)
# space - constant o(1)

print(max_value([-5, -2, -1, -11])) # -> -1
