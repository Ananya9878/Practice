for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    res=0
    for i in range(n):
        t = l[i] - i
        if t in d:
            d[t]+=1
        else:
            d[t] = 1
    for i in d:
        res+=((d[i]-1)*d[i])//2
    print(res)


    # c = 0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if (l[j]-l[i]) == (j-i):
    #             c+=1
    # print(c)

