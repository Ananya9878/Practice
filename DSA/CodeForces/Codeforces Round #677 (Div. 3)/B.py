for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    while l:
        if l[0] == 1:
            break
        if l[0] == 0:
            l.pop(0)


    while l:
        if l[-1] == 1:
            break
        if l[-1] == 0:
            l.pop()


    p = l.count(0)
    print(p)






