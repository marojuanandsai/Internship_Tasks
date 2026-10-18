from collections import Counter

x = int(input())
shoes = Counter(map(int, input().split()))

n = int(input())
money = 0

for i in range(n):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        money += price
        shoes[size] -= 1

print(money)
