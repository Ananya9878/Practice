for _ in range(int(input())):
    n,w,r = map(int,input().split())
    l2 = list(map(int,input().split()))


    d = {}
    for i in range(len(l2)):
        if l2[i] not in d:
            d[l2[i]] = 1
        else:
            d[l2[i]]+=1

    for i in d:
        if d[i]&1==0:
            r+=(i*d[i])
        else:
            r+=(i*(d[i]-1))
    if r>=w:
        print('YES')
    else:
        print('NO')

# 3
# 2 5 10
# 2 2
# 7 100 50
# 100 10 10 10 10 10 90
# 6 100 40
# 10 10 10 10 10 10
