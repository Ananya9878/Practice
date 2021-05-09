for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    arr = []
    while len(l)>0:
        arr.append(l.pop(0))
        if len(l)>0:
            arr.append(l.pop())

    print(*arr)
