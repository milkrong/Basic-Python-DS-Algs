def almost_palindromes(str):
    reversed_string = str[::-1]
    cnt = 0
    for i, j in zip(str, reversed_string):
        if i == j:
            continue
        else:
            cnt += 1
    return cnt

print(almost_palindromes("abcdcaa"))