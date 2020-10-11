for i in range(int(input())):
    n,m,s = list(map(int,input().split()))
    k = m%(n)
    k = (k+s-1)%(n)
    if k == 0:
        print(n)
    else:
        print(k)




