for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    flag = False
    for i in range(n):
        if l[i] not in d:
            d[l[i]] = [i]
        else:
            d[l[i]].append(i)

    for i in d:
        if len(d[i])>2:
            flag = True
            break
        if len(d[i])>=2:

            for j in range(1,len(d[i])):
                if d[i][j]-d[i][j-1]>1:
                    flag = True
                    break
            if flag:
                break
    if flag:
        print('YES')
    else:
        print('NO')