def caculate(s):
    """
    Implement a basic calculator to evaluate a simple expression string.
    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
    The integer division should truncate toward zero.
    :param s: string
    :return: int
    """
    if not s:
        return  []
    stack, num, sign = [], 0, "+"
    for i in range(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) -1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            else:
                tmp = stack.pop()
                if tmp // num < 0 and tmp % num !=0:
                    stack.append(tmp//num + 1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0

    return sum(stack)
