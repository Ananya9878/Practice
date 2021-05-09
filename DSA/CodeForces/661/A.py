for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    flag = True
    while len(l)>1:
        p = l[0]
        p1 = l[1]
        c = abs(p-p1)
        if c>1:
            print('NO')
            flag = False
            break
        else:
            l.pop(0)
    if flag:
        print('YES')
    # print(l)
