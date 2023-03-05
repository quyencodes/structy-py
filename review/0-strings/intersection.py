def intersection(a, b):
  values = set(a) # o(a)
  return [item for item in b if item in values]