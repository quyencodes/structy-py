def detect_dictionary(dictionary, alphabet):
  for i in range(0, len(dictionary) - 1):
    word_1, word_2 = dictionary[i], dictionary[i + 1]
    if not lexical_order(alphabet, word_1, word_2):
      return False

  return True

def lexical_order(alphabet, word_1, word_2):
  alphabet_set = {letter: index for index, letter in enumerate(alphabet)}

  max_length = max(len(word_1), len(word_2))

  for i in range(0, max_length):
    if i == len(word_1):
      return True
    if i == len(word_2):
      return False

    letter_1, letter_2 = alphabet_set[word_1[i]], alphabet_set[word_2[i]]
    if letter_1 < letter_2:
      return True
    elif letter_1 > letter_2:
      return False

  return True

def detect_dictionary(dictionary, alphabet):
  for i in range(0, len(dictionary) - 1):
    j = i + 1
    if not lexical_order(dictionary[i], dictionary[j], alphabet):
      return False

  return True

def lexical_order(word_1, word_2, alphabet):
  max_length = max(len(word_1), len(word_2))

  for i in range(0, max_length):
    val_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    val_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
    if val_1 < val_2:
      return True
    elif val_2 < val_1:
      return False

  return True