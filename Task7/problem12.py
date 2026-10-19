
def makingAnagrams(s1, s2):
    deletions = 0

    for char in "abcdefghijklmnopqrstuvwxyz":
        deletions += abs(s1.count(char) - s2.count(char))

    return deletions


s1 = input()
s2 = input()

print(makingAnagrams(s1, s2))
