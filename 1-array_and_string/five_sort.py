def five_sort(nums):
  i = 0
  j = len(nums) - 1

  while i <= j:
    if nums[j] is 5:
      j -= 1
    else:
      if nums[i] is 5:
        # do the swapping
        five = nums[i]
        not_five = nums[j]

        nums.pop(j)
        nums.pop(i)

        nums.insert(j, five)
        nums.insert(i, not_five)

      else:
        i += 1

  return nums