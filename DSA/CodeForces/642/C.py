for _ in range(int(input())):
    n = int(input())
    c = n//2
    res=0
    for i in range(1,c+1):
        p = i*(8*i)
        res+=p
    print(res)