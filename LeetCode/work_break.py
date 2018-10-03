def word_break(s, words):
    """
    check is break word list in the string s
    :param s:
    :param words:
    :return:
    """

    d = [False] * (len(s) + 1)
    d[0] = False
    for i in range(1, len(s) + 1):
        for w in words:
            if w == s[i-len(w):i] and d[i-len(w)]:
                d[i] = True
    return d[-1]