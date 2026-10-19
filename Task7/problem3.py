def marsExploration(s):
    count = 0
    expected = "SOS"

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            count += 1

    return count


s = input()
print(marsExploration(s))
