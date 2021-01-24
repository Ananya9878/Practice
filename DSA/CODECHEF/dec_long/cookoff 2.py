for _ in range(int(input())):
    x,y,k,n = list(map(int,input().split()))
    d = abs(x-y)
    if d%k == 0:
        s = d//k
        if s & 1 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

    # t=[]
    # p=[]
    # i = x
    # j = y
    # sp,st = k,k
    # while i<=n or j<=n:
    #     p.append(i)
    #     i+=sp
    #     t.append(j)
    #     j+=st
    # print(p,t)
    # for i in range(len(p)):
    #     if p[i] not in t:
    #         print('No')
    #         break
    #     else:
    #         print('Yes')
    #         break



    # print(t,p)
