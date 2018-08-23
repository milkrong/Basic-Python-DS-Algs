def reverse_vowels(strings):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i, j = 0, len(strings) - 1
    res = list(strings)
    while i<=j:
        ci, cj = strings[i], strings[j]
        if ci not in vowels:
            i += 1
        elif cj not in vowels:
            j -= 1
        else:
            res[i] = cj
            res[j] = ci
            i += 1
            j -= 1

    return ''.join(res)

print(reverse_vowels('leetcode'))