def tree(ino, pre):
    print(ino,pre)
    if len(ino) == 0:
        return None

    a = pre.pop(0)

    if len(ino) == 1:
        print(a)
        return None

    k = ino.index(a)
    left = ino[:k]
    right = ino[k + 1:]

    tree(left, pre)
    tree(right, pre)
    return None


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ino = sorted(arr)
    tree(ino, arr)

