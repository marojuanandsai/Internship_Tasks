#!/bin/python3

import math
import os
import random
import re




from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd_count = 0

    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


s = input().strip()
print(gameOfThrones(s))
