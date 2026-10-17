# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # The first line is the number of stamps
    n = int(input_data[0])
    
    # Use a set to store distinct country names
    stamps = set()
    
    # Add each country to the set
    for i in range(1, n + 1):
        if i < len(input_data):
            stamps.add(input_data[i].strip())
            
    # Print the total number of distinct stamps
    print(len(stamps))

if __name__ == '__main__':
    main()
