def group_anagram(strs):
    """
    Given an array of strings, group anagrams together.
    :param strs: list[strs]
    :return: list[list[strs]
    """
    ana = {}
    for string in strs:
        s = ''.join(sorted(string))
        if s in ana:
            ana[s].append(string)
        else:
            ana[s] = [string]
    return [ana[x] for x in ana]