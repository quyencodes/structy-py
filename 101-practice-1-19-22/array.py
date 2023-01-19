# Design a class that supports these 3 operations
# 1. inserting a value (no duplicates)
# 2. removing a value
# 3. getRandom a value that is already inserted (with equal probability)

# so let me just repeat the question back to you to make sure I understood it. From what I understand
import random
class Store:
  # constructor
  def __init__(self):
    self.map = set()

  def insert(self, value):
    self.map.add(value)

  def remove(self, value):
    self.map.remove(value)

  def get_random(self):
    return random.choice(list(self.map))

# more efficient get_random
import random
class Store:
  # constructor
  def __init__(self):
    self.map = {}
    self.values = []

  def insert(self, value):
    if value in self.map:
      return

    self.map[value] = len(self.values) - 1
    self.values.append(value)

  def remove(self, value):
    if value not in self.map:
      return

    index = self.map[value]
    last_element = self.values[-1]

    # array operations
    # perform swapping in array
    self.values[-1] = value
    self.values[index] = last_element

    # map operations
    # change the index in the dict
    self.map[last_element] = index
    # remove the value from the dict
    self.values.pop()
    del self.map[value]

  def get_random(self):
    return random.choice(self.values)

example_input = [3, 4, 4, 5]
self.values = [5, 4, 3]
self.map = {3: 0, 4: 1, 5: 0}
# remove(3)
# index = 0
# last_element = 5
# getrandom(self.list)

# handle duplicates more efficient get_random
import random
import collections
class Store:
  # constructor
  def __init__(self):
    self.map = collections.defaultdict(set)
    self.values = []

  def insert(self, value):
    self.values.append(value)
    self.map[value].add(len(self.values) - 1)

  def remove(self, value):
    if value not in self.map:
      return

    index = next(iter(self.map[value]))
    last_element = self.values[-1]

    # array operations
    # perform swapping in array
    self.values[-1] = value
    self.values[index] = last_element

    # map operations
    # change the index in the dict
    self.map[last_element].add(index)
    self.map[last_element].remove(len(self.values) - 1)
    # remove the value from the dict

    self.values.pop()
    self.map[value].remove(index)

  def get_random(self):
    return random.choice(self.values)

example_input = [3, 4, 4, 5]
self.values = [3, 5, 4]
self.map = {3: {0}, 4: {2}, 5: {1}}
# remove(4)
# index = 1
# last_element = 5
# getrandom(self.list)