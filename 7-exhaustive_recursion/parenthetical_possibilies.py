def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']

  all_possibilities = []
  choices, remainder = get_choices(s)
  for choice in choices:
    remainder_possibilities = parenthetical_possibilities(remainder) # []
    for possibility in remainder_possibilities:
      all_possibilities.append(choice + possibility)

  return all_possibilities

def get_choices(s): # (abc)de -> 'abc'
  if s[0] == '(':
    # group
    end = s.index(')')
    choices = s[1:end]
    remainder = s[end+1:]
    return (choices, remainder)
  else:
    # regular char
    return (s[0], s[1:])

print(get_choices('(abc)de'))
print(get_choices('(qrstuv)asdsads'))
print(get_choices('xyz'))
# def get_choices(s): # xyz -> 'x'

