from collections import deque
def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2
  left_sorted = merge_sort(nums[0:mid])
  right_sorted = merge_sort(nums[mid:])

  return merge(left_sorted, right_sorted)

def merge(list1, list2):
  list1 = deque(list1)
  list2 = deque(list2)

  merged = []

  while list1 and list2:
    if list1[0] < list2[0]:
      merged.append(list1.popleft())
    else:
      merged.append(list2.popleft())

  merged += list1
  merged += list2

  return merged
