k = int(input())
rooms = list(map(int, input().split()))

captain = (sum(set(rooms)) * k - sum(rooms)) // (k - 1)

print(captain)
