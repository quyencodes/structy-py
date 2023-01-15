def intersection(a, b):
  return list(set(a).intersection(b))

def intersection(a, b):
  set_A = set(a)
  return [item for item in b if item in set_A]

def intersection(a, b):
  result = []
  for num in b:
    if num in a:
      result.append(num)

  return result