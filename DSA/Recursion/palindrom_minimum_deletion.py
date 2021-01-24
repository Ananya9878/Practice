def count(s, i, j):
    print(s, i, j)
    if i > j:
        return 0
    if s[i] == s[j]:
        return count(s, i + 1, j - 1)
    a = count(s, i + 1, j)
    b = count(s, i, j - 1)
    return 1 + min(a, b)


for _ in range(int(input())):
    s = input()
    t = count(s, 0, len(s) - 1)
    print(t)
