
#!/bin/python3

import os

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    previous = ""

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous = char

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    n = int(input().strip())

    queries = []
    for _ in range(n):
        queries.append(int(input().strip()))

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
