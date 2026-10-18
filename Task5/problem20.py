t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    top = float('inf')
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            cube = blocks[left]
            left += 1
        else:
            cube = blocks[right]
            right -= 1

        if cube > top:
            possible = False
            break

        top = cube

    print("Yes" if possible else "No")
