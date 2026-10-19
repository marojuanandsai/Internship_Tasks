
#!/bin/python3

import os
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    freq1 = Counter(s1)
    freq2 = Counter(s2)

    changes = 0

    for char in freq1:
        if freq1[char] > freq2[char]:
            changes += freq1[char] - freq2[char]

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
