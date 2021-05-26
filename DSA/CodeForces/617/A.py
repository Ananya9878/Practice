for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    o = [i for i in a if i&1]
    e = [i for i in a if i&1==0]
    l = sum(a)
    if l&1:
        print('YES')
    else:
        if len(e)>0 and len(o)>0:
            print('YES')
        else:
            print('NO')