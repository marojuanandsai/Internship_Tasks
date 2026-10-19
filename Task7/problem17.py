def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        formed = str(first)

        while len(formed) < len(s):
            current += 1
            formed += str(current)

        if formed == s:
            print("YES", first)
            return

    print("NO")
