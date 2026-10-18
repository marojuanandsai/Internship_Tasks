from collections import Counter

s = input()

counts = Counter(s)

result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

for char, count in result[:3]:
    print(char, count)
