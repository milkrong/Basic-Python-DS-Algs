def bracket_match(bracket_string):
    res = 0
    for b in bracket_string:
        if b == "(":
            res += 1
        elif b == ")":
            res -= 1
        else:
            continue
    res = 0 if res ==0 else 1     
    return res


print(bracket_match("(((())"))