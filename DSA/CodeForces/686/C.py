'''
1 3 1 4 1 2
1: 3
3: 2
4:2
2:1
1 3 4 1 1 2
1:2[0,3,4]
2:1[5]
3:2[1]
4:2[2]
'''
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in range(n):
        if l[i] not in d:
            d[l[i]] = [i]
        else:
            d[l[i]].append(i)

    s = 10000000

    for i in d:
        res = 0
        p = d[i]
        for i in range(len(p)-1):
            c = p[i+1] - p[i]
            if c>1:
                res+=1
        if p[-1] != n-1:
            res+=1
        if p[0] != 0:
            res+=1
        if s>res:
            s = res
    print(s)









