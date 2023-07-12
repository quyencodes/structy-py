def token_transform(s, tokens, seen={}):
    i, j = 0, 1
    res = []
    while i < len(s):
        if s[i] != '$':
            res.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i:j + 1]
            word = seen[tokens[key]] if tokens[key] in seen else token_transform(
                tokens[key], tokens, seen)
            seen[tokens[key]] = word
            res.append(word)
            i = j + 1
            j = i + 1

    return ''.join(res)
