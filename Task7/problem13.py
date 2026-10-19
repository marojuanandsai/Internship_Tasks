
#!/bin/python3

import os
from collections import Counter

def isValid(s):
    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) != 2:
        return "NO"

    (f1, c1), (f2, c2) = freq_count.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"

    if f1 > f2 and f1 - f2 == 1 and c1 == 1:
        return "YES"

    if f2 > f1 and f2 - f1 == 1 and c2 == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
