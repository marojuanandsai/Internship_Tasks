
#!/bin/python3

import os

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for char in s:
        if char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            result += char

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = input()
    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()
