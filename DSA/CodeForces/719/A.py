for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    flag  = True
    for i in d:
        p = d[i]
        for i in range(len(p)-1):
            c = p[i+1]-p[i]
            if c>1:
                print('NO')
                flag = False
                break
        if flag == False:
            break
    if flag:
        print('YES')

