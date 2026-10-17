# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

# Find symmetric difference using the symmetric_difference() method (or the ^ operator)
sym_diff = a.symmetric_difference(b)

# Print each element in ascending order, one per line
for num in sorted(sym_diff):
    print(num)
