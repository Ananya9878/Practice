for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p = []
    for i in l:
        if i not in p:
            p.append(i)
    print(*p)