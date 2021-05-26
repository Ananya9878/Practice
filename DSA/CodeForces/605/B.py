for _ in range(int(input())):
    s = input()
    l,r,u,d = s.count('L'),s.count('R'),s.count('U'),s.count('D')
    m1,m2 = min(l,r),min(u,d)
    res = m1*2+m2*2
    if m1>0 and m2>0:
        g = 'L'*m1+'U'*m2+'R'*m1+'D'*m2
        print(res)
        print(g)
    elif m1>0:
        g = 'LR'
        print(2)
        print(g)
    elif m2>0:
        g = 'UD'
        print(2)
        print(g)
    else:
        print(0)


