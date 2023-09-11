"""
Create a hashmap to find the order of the alphabet. Use two pointers and check each letter 1 by 1 for word_1 and word_2. While loop should have OR operator and inside if i or j hit the end of its respective word, return boolean value
"""


def lexical_order(word_1, word_2, alphabet):
  alphaMap = {alphabet[i]: i for i in range(len(alphabet))}

  i, j = 0, 0

  while i < len(word_1) or j < len(word_2):
    if i == len(word_1):
      return True

    if j == len(word_2):
      return False

    letter_1, letter_2 = word_1[i], word_2[j]

    if alphaMap[letter_1] < alphaMap[letter_2]:
      return True
    elif alphaMap[letter_1] > alphaMap[letter_2]:
      return False

    i += 1
    j += 1

  return True
