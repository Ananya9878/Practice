for _ in range(int(input())):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    p = list(map(int,input().split()))
    flag = True
    while flag:
        flag = False
        for i in p:
            if i<n:
                if l[i-1] > l[i]:
                    l[i],l[i-1] = l[i-1],l[i]
                    flag = True
    if l == sorted(l):
        print('YES')
    else:
        print('NO')



