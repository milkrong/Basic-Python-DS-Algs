def length_of_longest_substring(s):
    dic = {}
    ans = start = 0
    for i, v in enumerate(s):
        if v not in dic or dic[v] < start:
            ans = max(ans, i - start + 1)
        else:
            start = dic[v] + 1

        dic[v] = i

    return ans 
