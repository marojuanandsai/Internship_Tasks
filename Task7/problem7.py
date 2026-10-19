
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]

        row = "-".join(left + right)
        row = row.center(4 * size - 3, "-")
        lines.append(row)

    print("\n".join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
