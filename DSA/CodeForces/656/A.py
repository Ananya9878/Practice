for i in range(int(input())):
    x,y,z = map(int,input().split())
    m = max(x,y,z)
    m1 = min(x,y,z)
    c = [x,y,z].count(m)

    if c>1:
        print('YES')
        print(m,m1,m1)
    else:
        print('NO')