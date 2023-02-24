def combine_intervals(intervals):
  sorted_intervals = sort_intervals(intervals)
  merged_intervals = []
  for interval in sorted_intervals:
    curr_a, curr_b = interval
    if len(merged_intervals) == 0:
      merged_intervals.append(interval)
    else:
      last_a, last_b = merged_intervals[-1]
      if curr_a <= last_b:
        last_b = max(curr_b, last_b)
        merged_intervals[-1] = (last_a, last_b)
      else:
        merged_intervals.append(interval)
  return merged_intervals

def sort_intervals(intervals):
  map = {} # key: a, value: ()

  for interval in intervals:
    a, b = interval
    map[a] = interval

  keys_sorted = sorted(map.keys()) # [1, 3, 8, 12]

  sorted_intervals = []
  for key in keys_sorted:
    sorted_intervals.append(map[key])

  return sorted_intervals


intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
print(combine_intervals(intervals))
# -> [ (1, 7), (8, 15) ]