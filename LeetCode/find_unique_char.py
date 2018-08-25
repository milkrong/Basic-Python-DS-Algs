def first_uniq_char(s):
    chars = set(s)
    return min([s.find(c) for c in chars if s.count(c) == 1] or [-1])