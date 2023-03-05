# time - o(n), where n is the number of ints in the list
# space - o(1)
def five_sort(nums):
  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] != 5:
      i += 1
    else:
      nums[i], nums[j] = nums[j], nums[i]

  return nums


"""
[12, 7, 1, 12, 5, 5]
           i
               j

[12, 7, 1, 5, 12, 5]
"""