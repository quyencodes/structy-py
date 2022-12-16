def intersection(a, b):
  # create a set
  myset = set(a)
  return list(myset.intersection(b))

# def intersection(a, b):
#   # create a set
#   intersections = []
#   myset = set(a)
#   for number in b:
#     if number in myset:
#       intersections.append(number)

#   return intersections

def intersection(list1, list2):
  # set constructor
  items_set = set(list1)
  # return statement
  return [ ele for ele in list2 if ele in items_set]