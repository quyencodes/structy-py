"""
Check two words at a time. Have a helper function determine with inputs word_1 and word_2 to see if these 2 words are ordered properly. Main function iterates through the dictionary and passes two words at a time to the main function.
"""


def detect_dictionary(dictionary, alphabet):
  for i in range(len(dictionary) - 1):
    j = i + 1
    word_1, word_2 = dictionary[i], dictionary[j]

    if not lexical_order(alphabet, word_1, word_2):
      return False

  return True


def lexical_order(alphabet, word_1, word_2):
  alphaMap = {letter: index for index, letter in enumerate(alphabet)}

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
