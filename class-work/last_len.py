def last_len(string):
    words = string.split()
    last_word = words[-1]
    return len(last_word)


print(last_len('i love you'))