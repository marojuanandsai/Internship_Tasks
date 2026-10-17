from collections import Counter

# Read number of shoes and the shoe size list
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))

# Read number of customers
num_customers = int(input())

# Count available shoes using Counter
inventory = Counter(shoe_sizes)
total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    # Check if the shoe size is in stock
    if inventory[size] > 0:
        total_earned += price
        inventory[size] -= 1  # Reduce the count of that shoe size

# Print total money earned
print(total_earned)
