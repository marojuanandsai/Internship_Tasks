# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # n: size of the array, m: size of sets A and B
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Read the array elements
    arr = input_data[2:2+n]
    
    # Read sets A and B as sets for O(1) average-time complexity lookup
    # Using generator expressions with set() avoids storing intermediate lists
    set_a = set(input_data[2+n : 2+n+m])
    set_b = set(input_data[2+n+m : 2+n+2*m])
    
    # Calculate happiness
    # (x in set_a) evaluates to 1 if True, 0 if False
    happiness = sum((1 if x in set_a else -1 if x in set_b else 0) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
