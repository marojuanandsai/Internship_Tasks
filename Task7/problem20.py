
#!/bin/python3

import os

def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return ''.join(stack)
    else:
        return "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    result = superReducedString(s)

    fptr.write(result + '\n')
    fptr.close()
