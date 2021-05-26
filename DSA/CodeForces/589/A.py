for _ in range(int(input())):
    a,b,n,s = map(int,input().split())
    p = s//n
    k = min(p,a)
    c = k*n
    c1 = c+b
    if c1>=s:
        print('YES')
    else:
        print('NO')




    # if m == s:
    #     print('YES')
    # else:
    #     l = set([0])
    #     for i in range(1,a+1):
    #         for j in range(1,b+1):
    #             p = n*i+j
    #             l.add(p)
    #     print(l)
    #     if a*n+a>=s:
    #         if a*n+a in l:
    #             print('YES')
    #         else:
    #             print('NO')
    #     else:
    #         print('NO')




