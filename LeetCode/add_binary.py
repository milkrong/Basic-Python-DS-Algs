def add_binary(a, b):
    '''

    :param a: str
    :param b: str
    :return: str
    '''
    result = ''
    index = 0

    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'

        val = int(num_a) + int(num_b) + int(carry)
        result = "%s%s" % (val % 2, result)

        carry = '1' if val > 1 else '0'
        index += 1

    return result

