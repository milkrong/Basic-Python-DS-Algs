import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING encoded as parameter.
#

def decode(encoded):
    # Write your code here
    i = 0
    result = []
    ascii_string = encoded[::-1]
    while i < len(ascii_string):
        if ascii_string[i] == "1":
            result.append(int(ascii_string[i:i+3]))
            i += 3
        else:
            result.append(int(ascii_string[i:i+2]))
            i += 2

    result = list(map(chr, result))

    return result

print(decode("1219950180111108236115111016623101401611235115012312161151110101111127"))