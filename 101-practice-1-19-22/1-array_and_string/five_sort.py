def five_sort(nums):
  i = 0
  j = len(nums) - 1

  while i <= j:
    if nums[j] == 5:
      j -= 1
    else:
      if nums[i] == 5:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i += 1
  return nums

#.       i  j
# [4, 1, 1, 1, 5, 5, 5]

# practice longest palindrome